#!/usr/bin/env python3
"""Validate this 15-pet collection using Python 3.9+ and the standard library."""

import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys


EXPECTED_IDS = {
    "erdu": "erdu",
    "hanli-2": "hanli",
    "yinyue-yitong": "yinyue-yitong",
    "xuangu": "xuangu",
    "song-yu": "song-yu",
    "wang-chan-wheelchair": "wang-chan-wheelchair",
    "fengxi": "fengxi",
    "nanlonghou": "nanlonghou",
    "yinyue-fox": "yinyue-fox",
    "wen-tianren": "wen-tianren",
    "yinyue-3": "yinyue",
    "ziling": "ziling",
    "caicai": "caicai",
    "cc-cat-3": "cc-cat",
    "gulu": "gulu",
}
PAYLOAD_FILES = {"pet.json", "spritesheet.webp"}
RESERVED_NAMES = {"con", "prn", "aux", "nul"} | {
    f"{prefix}{number}" for prefix in ("com", "lpt") for number in range(1, 10)
}


class ValidationError(ValueError):
    """An invalid manifest, package, or filesystem path."""


def repository_root():
    return Path(os.path.abspath(__file__)).parent.parent


def is_link(path):
    """Detect symbolic links and Windows junctions/reparse points."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0) & 0x400
    )


def require_plain_path(path):
    """Reject links in every existing path component before reading/writing."""
    for component in reversed((path, *path.parents)):
        if is_link(component):
            raise ValidationError(f"Linked or reparse-point path is not allowed: {component}")


def safe_identifier(value, label):
    if (
        not isinstance(value, str)
        or not re.fullmatch(r"[a-z0-9][a-z0-9_-]{0,79}", value)
        or value.lower() in RESERVED_NAMES
    ):
        raise ValidationError(f"Unsafe {label}: {value!r}")
    return value


def safe_child(parent, name):
    """Allow one relative filename only, with a path inside its parent."""
    if (
        not isinstance(name, str)
        or not name
        or name in (".", "..")
        or any(character in name for character in ('/', '\\', ':', '\x00'))
        or name.endswith((".", " "))
        or name.split(".", 1)[0].lower() in RESERVED_NAMES
    ):
        raise ValidationError(f"Unsafe relative path: {name!r}")
    result = parent / name
    require_plain_path(result)
    if result.resolve().parent != parent.resolve():
        raise ValidationError(f"Path escapes its parent: {result}")
    return result


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(data, label):
    try:
        result = json.loads(data.decode("utf-8-sig"), object_pairs_hook=_unique_object)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ValidationError(f"Invalid JSON in {label}: {error}") from error
    if not isinstance(result, dict):
        raise ValidationError(f"{label} must be a JSON object")
    return result


def load_catalog(root):
    """Check metadata, the exact published roster, and package directories."""
    require_plain_path(root)
    catalog_path = safe_child(root, "catalog.json")
    catalog = parse_json(catalog_path.read_bytes(), "catalog.json")
    if type(catalog.get("schemaVersion")) is not int or catalog["schemaVersion"] != 1:
        raise ValidationError("catalog.json must have schemaVersion: 1")
    for field in ("updatedAt", "author", "source"):
        if not isinstance(catalog.get(field), str) or not catalog[field].strip():
            raise ValidationError(f"Missing catalog field: {field}")
    entries = catalog.get("pets")
    if not isinstance(entries, list) or len(entries) != len(EXPECTED_IDS):
        raise ValidationError("The collection must contain exactly 15 published pets")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValidationError("Every pets entry must be an object")
        slug = safe_identifier(entry.get("slug"), "slug")
        pet_id = safe_identifier(entry.get("id"), "pet id")
        if slug in seen or EXPECTED_IDS.get(slug) != pet_id:
            raise ValidationError(f"Duplicate, unknown, or incorrectly mapped pet: {slug}")
        seen.add(slug)
        for field in ("name", "description", "category", "petdexUrl"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise ValidationError(f"{slug}: missing or invalid {field}")
        if not isinstance(entry.get("spriteVersion"), (str, int)) or isinstance(
            entry["spriteVersion"], bool
        ):
            raise ValidationError(f"{slug}: missing or invalid spriteVersion")
        files = entry.get("files")
        if not isinstance(files, dict) or set(files) != PAYLOAD_FILES:
            raise ValidationError(f"{slug}: files must list pet.json and spritesheet.webp only")
        for filename, metadata in files.items():
            if not isinstance(metadata, dict):
                raise ValidationError(f"{slug}/{filename}: invalid file metadata")
            digest = metadata.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[a-fA-F0-9]{64}", digest):
                raise ValidationError(f"{slug}/{filename}: invalid SHA-256")
            if type(metadata.get("bytes")) is not int or metadata["bytes"] <= 0:
                raise ValidationError(f"{slug}/{filename}: invalid byte count")
    if seen != set(EXPECTED_IDS):
        raise ValidationError("The published roster is incomplete")
    pets_dir = safe_child(root, "pets")
    if not pets_dir.is_dir():
        raise ValidationError("The pets directory is missing")
    actual = set()
    for path in pets_dir.iterdir():
        require_plain_path(path)
        if not path.is_dir():
            raise ValidationError(f"Unexpected file in pets/: {path.name}")
        actual.add(path.name)
    if actual != seen:
        raise ValidationError(
            f"pets/ does not match catalog: missing={sorted(seen - actual)}, "
            f"extra={sorted(actual - seen)}"
        )
    return catalog


def validate_pet(root, entry):
    """Return the exact verified bytes to install; never re-read unchecked data."""
    slug = entry["slug"]
    pet_dir = safe_child(safe_child(root, "pets"), slug)
    paths = list(pet_dir.iterdir())
    if {path.name for path in paths} != PAYLOAD_FILES:
        raise ValidationError(f"{slug}: unexpected or missing package files")
    payloads = {}
    for filename in sorted(PAYLOAD_FILES):
        path = safe_child(pet_dir, filename)
        if not path.is_file():
            raise ValidationError(f"{slug}/{filename}: not a regular file")
        data = path.read_bytes()
        metadata = entry["files"][filename]
        if len(data) != metadata["bytes"]:
            raise ValidationError(f"{slug}/{filename}: byte count mismatch")
        if hashlib.sha256(data).hexdigest() != metadata["sha256"].lower():
            raise ValidationError(f"{slug}/{filename}: SHA-256 mismatch")
        payloads[filename] = data
    config = parse_json(payloads["pet.json"], f"{slug}/pet.json")
    for field in ("id", "displayName", "description", "spritesheetPath"):
        if not isinstance(config.get(field), str) or not config[field].strip():
            raise ValidationError(f"{slug}/pet.json: missing or invalid {field}")
    safe_identifier(config["id"], "pet.json id")
    if config["id"] != entry["id"]:
        raise ValidationError(f"{slug}: catalog id and pet.json id disagree")
    safe_child(pet_dir, config["spritesheetPath"])
    if config["spritesheetPath"] != "spritesheet.webp":
        raise ValidationError(f"{slug}: spritesheetPath must be spritesheet.webp")
    return payloads


def main():
    try:
        root = repository_root()
        catalog = load_catalog(root)
        total = 0
        for entry in catalog["pets"]:
            payloads = validate_pet(root, entry)
            total += sum(len(data) for data in payloads.values())
            print(f"OK {entry['slug']} -> {entry['id']}")
        print(f"Validated {len(catalog['pets'])} pets, 30 files, {total:,} bytes.")
        return 0
    except (OSError, ValidationError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
