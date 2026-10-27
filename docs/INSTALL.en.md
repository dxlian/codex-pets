# Installation, updates, and removal

[Back to the collection](../README.en.md) · [简体中文](INSTALL.zh-CN.md)

This repository contains configuration files and sprite sheets for 15 pets, plus an offline installer.
It is an asset collection; a compatible client provides the display, animation playback, and desktop interaction.

## 1. Requirements

- Use a Codex desktop client that supports custom pets. Available features depend on your installed client version.
- The scripts require **Python 3.9 or newer** and use only the standard library. No `pip install` is needed.
- Cloning requires Git; downloading a ZIP does not.
- Commands below cover Windows PowerShell and macOS / Linux terminals. The scripts are cross-platform; this does not imply an official desktop client is available on every platform.

Check Python in Windows PowerShell:

```powershell
py -3 --version
```

Check Python on macOS / Linux:

```sh
python3 --version
```

If the command is unavailable, install Python from the [official Python website](https://www.python.org/downloads/), then reopen your terminal.
On Windows, if `python --version` already reports Python 3.9+, you can replace `py -3` with `python` throughout this guide.

## 2. Download the complete repository

**Option A: ZIP download.** Open [Download ZIP](https://github.com/dxlian/codex-pets/archive/refs/heads/main.zip), extract everything, enter the `codex-pets-main` folder, and open a terminal there.
Do not run the scripts inside the ZIP archive or download only the preview GIFs.

**Option B: Git clone.** These commands work in Windows PowerShell and macOS / Linux terminals:

```sh
git clone https://github.com/dxlian/codex-pets.git
cd codex-pets
```

Run the following commands from the repository root. It should contain `catalog.json`, `scripts/`, and `pets/` together.
Once the download is complete, Python validation and installation work offline.

## 3. Validate, preview, and install all pets

Windows PowerShell:

```powershell
py -3 scripts/validate.py
py -3 scripts/install.py --dry-run
py -3 scripts/install.py
```

macOS / Linux:

```sh
python3 scripts/validate.py
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

The first command checks the directories, configuration, file sizes, and SHA-256 hashes for all 15 pets. Successful output ends with `Validated 15 pets, 30 files, ...`.
The second command reports the destination and planned actions without creating files.
The third installs all 15 pets. The installer verifies every selected package before writing and preserves the original `pet.json` files.

## 4. Install one pet or a selection

`--pet` accepts a **Petdex slug** and may be repeated. Omitting it selects all pets.

```powershell
# Windows: install 韩立（Han Li）
py -3 scripts/install.py --pet hanli-2
# Windows: install 二嘟（Erdu）, 韩立（Han Li）, and CC猫（CC Mao）
py -3 scripts/install.py --pet erdu --pet hanli-2 --pet cc-cat-3
```

```sh
# macOS / Linux: install 韩立（Han Li）
python3 scripts/install.py --pet hanli-2
# macOS / Linux: install 二嘟（Erdu）, 韩立（Han Li）, and CC猫（CC Mao）
python3 scripts/install.py --pet erdu --pet hanli-2 --pet cc-cat-3
```

See the [collection catalog](../README.en.md) for all available slugs. Repeating the same slug does not install it twice.
Add `--dry-run` to any installation command to preview it, for example `py -3 scripts/install.py --pet erdu --dry-run`.

## 5. Destination and CODEX_HOME

| Setting | Installation root |
| --- | --- |
| `CODEX_HOME` is not set | `.codex/pets/` under the current user's home directory |
| `CODEX_HOME` is set | `pets/` under the directory specified by `CODEX_HOME` |
| `--dest` is supplied | The specified directory directly; this takes priority over both defaults |

The usual Windows default is `C:\Users\<username>\.codex\pets\`; on macOS / Linux it is `~/.codex/pets/`.
Each pet gets a subdirectory named after its original id. Point `--dest` at the **pets root**, without adding an individual pet id.

These commands install one pet into a separate test directory:

```powershell
py -3 scripts/install.py --pet erdu --dest "$env:USERPROFILE\codex-pets-test"
```

```sh
python3 scripts/install.py --pet erdu --dest "$HOME/codex-pets-test"
```

The client does not automatically load this test directory. For normal use, install into the configuration directory your client actually uses.
To use a custom `CODEX_HOME`, you can first preview the destination in your current terminal:

```powershell
$env:CODEX_HOME = "D:\CodexData"
py -3 scripts/install.py --dry-run
```

```sh
CODEX_HOME="$HOME/.codex-custom" python3 scripts/install.py --dry-run
```

These examples do not change the client's own configuration directory for you.
The installer rejects destinations inside this repository, filesystem roots, and paths containing symbolic links or Windows junctions. Use ordinary directories.

## 6. Install an individual pet manually

You can copy the files manually without using the Python installer. Running the integrity check first is recommended.
For 韩立（Han Li）, the repository slug is `hanli-2`, while the id inside `pet.json` is `hanli`:

1. Open `pets/hanli-2/` in the repository and confirm it contains `pet.json` and `spritesheet.webp`.
2. Locate the client's pets root. The default is `~/.codex/pets/`; see the previous section for custom locations.
3. If a `hanli` folder already exists there, follow the conflict instructions below before copying anything over it.
4. Create a `hanli` folder under the pets root and place the two files directly inside it.

The correct structure is below. Do not add another `hanli-2` folder or a second `pets` level:

```text
.codex/
└── pets/
    └── hanli/
        ├── pet.json
        └── spritesheet.webp
```

The other differing mappings are `cc-cat-3 → cc-cat` and `yinyue-3 → yinyue`.
For every pet, use its `pet.json` id as the installation directory name and preserve the filenames and configuration.
After installation, reopen the client and select the pet in its pet selection interface. The exact entry point depends on the client version.
The installation script does not change your currently selected pet.

## 7. Existing files, updates, and conflicts

| Output | Meaning |
| --- | --- |
| `INSTALLED` | A new directory was created and the pet files were written |
| `SKIP` | The destination contains exactly the same two files; no installation is needed |
| `CONFLICT` | Existing content differs, contains extra files, or is not an ordinary directory; it is preserved |
| `WOULD INSTALL` | A dry-run preview; nothing has been written |

The installer never overwrites conflicts and has no `--force` option. Other eligible pets can still be installed when one pet has a conflict.
For example, keeping an extra backup file inside a pet's folder also counts as a conflict.

To update the repository, run `git pull --ff-only` in a Git checkout with no local changes you need to preserve. ZIP users can download and extract a fresh copy into a new folder.
Then run validation and `--dry-run` again. Identical installed versions are skipped; different versions require a manual decision:

1. Close the client and confirm the exact id and destination shown in the conflict report.
2. Copy that entire id folder to a location **outside the pets root**, such as a personal backup directory. Check that both files were backed up.
3. Once the backup is confirmed, move the old id folder out of the pets root to free its original location. Do not simply rename it inside pets.
4. Run the installation command for that pet again, reopen the client, and check it. To restore, move the new folder out and move the backup back into place.

You perform these backup, move, and restore steps yourself; the scripts do not do them automatically.

### Exit codes

| Code | Meaning |
| --- | --- |
| `0` | Validation passed, or installation / dry-run completed without conflicts; skipping identical files is also success |
| `1` | A validation, path, or file operation failed; read the error message |
| `2` | Installation encountered conflicts; invalid command-line argument syntax may also cause the argument parser to return `2` |

After a command, inspect `$LASTEXITCODE` in Windows PowerShell or run `echo $?` on macOS / Linux.
The validator normally returns `0` or `1`. After an installation error, read the output rather than assuming that either none or all of the pets were installed.

## 8. Remove a pet

Close the client, confirm the pet's **original id**, and remove only that specific folder from the pets root. Then reopen the client.
For example, 韩立（Han Li） uses `hanli`, not the repository slug `hanli-2`. Back up the folder outside pets first if you want to keep it.
Do not remove the entire `.codex` or `pets` directory. This repository has no automatic uninstall command and will not delete installed files for you.

## 9. Troubleshooting

**Python is missing or too old.** Install Python 3.9+ and reopen the terminal. Check `py -3 --version` on Windows or `python3 --version` on macOS / Linux.

**Validation fails.** Use the error output to identify the file, then download a complete fresh copy of the repository and retry. Do not change hashes in `catalog.json` to bypass the error. Keep backups and extra pets out of the source package directories.

**Installation succeeded, but the pet is missing in the client.** Confirm that the client supports custom pets and uses the same user account and `CODEX_HOME`. Check the `<pets-root>/<id>/pet.json` structure and reopen the client. A separate test directory is not loaded automatically.

**Two foxes have the same display name.** `yinyue-fox` and `yinyue-3` have different appearances, but both original display names may be “银月狐狸”. Their installed ids are `yinyue-fox` and `yinyue`; use the previews to distinguish them.

**The client does not show the Chinese names used in the documentation.** The collection labels these pets 二嘟（Erdu） (`erdu`), 财财（Caicai） (`caicai`), and 咕噜（Gulu） (`gulu`). The client still reads the original `displayName` in `pet.json`, so it may show `erdu`, `caicai`, and `gulu`. Documentation names do not change the configuration or installation ids.

**The preview GIF differs from the animation in the client.** Repository GIFs provide a quick preview. The client determines the actual motions and playback speed from the sprite sheet.

## 10. Install through Petdex

You can also use the client or CLI described in the [official Petdex documentation](https://petdex.dev/docs). With Node.js / npm available, an official CLI example is:

```sh
npx petdex install erdu
```

This is a separate Petdex installation flow. It uses the network and does not run this repository's Python installer.
Its destinations, supported platforms, and overwrite behavior are governed by Petdex's documentation; the Python installer rules on this page do not apply to that flow.

[Back to the collection](../README.en.md) · [简体中文](INSTALL.zh-CN.md)
