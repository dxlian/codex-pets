#!/usr/bin/env python3
"""Install verified desktop pets without replacing existing files (Python 3.9+)."""

import argparse
import os
from pathlib import Path
import sys

# Keep --dry-run free of filesystem writes, including Python import caches.
sys.dont_write_bytecode = True

from validate import (
    ValidationError,
    is_link,
    load_catalog,
    repository_root,
    require_plain_path,
    safe_child,
    validate_pet,
)


def default_destination():
    codex_home = os.environ.get("CODEX_HOME")
    return (Path(codex_home).expanduser() if codex_home else Path.home() / ".codex") / "pets"


def existing_status(target, payloads):
    """Only an ordinary directory containing the same two files is identical."""
    if is_link(target):
        return "conflict"
    if not target.exists():
        return "new"
    if not target.is_dir():
        return "conflict"
    if {path.name for path in target.iterdir()} != set(payloads):
        return "conflict"
    for filename, data in payloads.items():
        path = target / filename
        if is_link(path) or not path.is_file() or path.read_bytes() != data:
            return "conflict"
    return "identical"


def install_new(target, payloads):
    """Reserve a new directory and create files exclusively; never overwrite."""
    require_plain_path(target.parent)
    target.mkdir()  # Raises FileExistsError if another process created it.
    for filename, data in payloads.items():
        path = safe_child(target, filename)
        with path.open("xb") as output:
            output.write(data)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pet", action="append", metavar="SLUG",
        help="Install one Petdex slug; repeat this option to select several (default: all 15)",
    )
    parser.add_argument(
        "--dest", type=Path, default=None, metavar="DIRECTORY",
        help="Destination pets directory (default: $CODEX_HOME/pets or ~/.codex/pets)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Validate files and report planned actions without creating anything",
    )
    args = parser.parse_args(argv)
    try:
        root = repository_root()
        catalog = load_catalog(root)
        entries = {entry["slug"]: entry for entry in catalog["pets"]}
        requested = list(dict.fromkeys(args.pet or entries))
        unknown = set(requested) - set(entries)
        if unknown:
            raise ValidationError(
                f"Unknown pet slug(s): {', '.join(sorted(unknown))}. "
                f"Choose from: {', '.join(entries)}"
            )
        # Verify every selected package before making any filesystem changes.
        verified = {
            slug: validate_pet(root, entries[slug]) for slug in requested
        }
        supplied = args.dest if args.dest is not None else default_destination()
        destination = Path(os.path.abspath(supplied.expanduser()))
        require_plain_path(destination)
        if destination == Path(destination.anchor):
            raise ValidationError("The filesystem root cannot be an installation destination")
        if destination.resolve().is_relative_to(root.resolve()):
            raise ValidationError("Choose a destination outside the collection repository")
        if destination.exists() and not destination.is_dir():
            raise ValidationError(f"Destination is not a directory: {destination}")
        print(f"Destination: {destination}")
        installed = skipped = conflicts = 0
        for slug in requested:
            pet_id = entries[slug]["id"]
            target = destination / pet_id
            # The id was checked against the roster and a safe single-name grammar.
            if target.parent != destination:
                raise ValidationError(f"Unsafe installation target: {target}")
            status = existing_status(target, verified[slug])
            if status == "conflict":
                print(f"CONFLICT {slug} -> {pet_id}: existing files left unchanged")
                conflicts += 1
            elif status == "identical":
                print(f"SKIP {slug} -> {pet_id}: already installed (identical)")
                skipped += 1
            elif args.dry_run:
                print(f"WOULD INSTALL {slug} -> {pet_id}")
                installed += 1
            else:
                require_plain_path(destination)
                destination.mkdir(parents=True, exist_ok=True)
                try:
                    install_new(target, verified[slug])
                except FileExistsError:
                    print(f"CONFLICT {slug} -> {pet_id}: target appeared; no files replaced")
                    conflicts += 1
                    continue
                print(f"INSTALLED {slug} -> {pet_id}")
                installed += 1
        verb = "would install" if args.dry_run else "installed"
        print(f"Done: {verb} {installed}, identical {skipped}, conflicts {conflicts}.")
        return 2 if conflicts else 0
    except (OSError, ValidationError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
