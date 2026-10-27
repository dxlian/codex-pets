# 安装、更新与卸载

[返回合集](../README.md) · [English](INSTALL.en.md)

本仓库保存 15 只桌宠的配置与精灵图，并提供离线安装脚本。
它是资源合集；显示、动画播放和桌面交互由支持此格式的客户端提供。

## 1. 准备环境

- 使用支持自定义桌宠的 Codex 桌面客户端，具体功能以你安装的客户端版本为准。
- 脚本需要 **Python 3.9 或更新版本**，仅使用标准库，无需 `pip install`。
- 用 Git 下载需要安装 Git；使用 ZIP 下载无需 Git。
- 下文提供 Windows PowerShell 和 macOS / Linux 的终端命令。脚本可跨平台运行，不代表所有平台都有可用的官方桌面客户端。

在 Windows PowerShell 检查 Python：

```powershell
py -3 --version
```

在 macOS / Linux 检查 Python：

```sh
python3 --version
```

如果命令不存在，先从 [Python 官网](https://www.python.org/downloads/) 安装 Python，再重新打开终端。
如果 Windows 已能通过 `python --version` 调用 Python 3.9+，也可将以下 `py -3` 替换为 `python`。

## 2. 下载整个仓库

**方式 A：下载 ZIP。** 打开 [Download ZIP](https://github.com/dxlian/codex-pets/archive/refs/heads/main.zip)，完整解压后进入 `codex-pets-main` 文件夹，并在该文件夹打开终端。
不要直接在压缩包内运行脚本，也不要只下载预览 GIF。

**方式 B：使用 Git。** Windows PowerShell 和 macOS / Linux 均可执行：

```sh
git clone https://github.com/dxlian/codex-pets.git
cd codex-pets
```

以下命令均从仓库根目录运行。当前位置应同时包含 `catalog.json`、`scripts/` 和 `pets/`。
完整下载后，Python 校验和安装过程无需联网。

## 3. 校验、预览并安装全部桌宠

Windows PowerShell：

```powershell
py -3 scripts/validate.py
py -3 scripts/install.py --dry-run
py -3 scripts/install.py
```

macOS / Linux：

```sh
python3 scripts/validate.py
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

第一条命令检查 15 只桌宠的目录、配置、文件大小和 SHA-256；成功时最后显示 `Validated 15 pets, 30 files, ...`。
第二条命令显示目标路径及计划动作，不创建文件。
第三条命令安装全部 15 只。安装器会在写入前验证所有选中的资源，并保留原始 `pet.json`。

## 4. 只安装一只或指定几只

`--pet` 使用 **Petdex slug**，可重复指定；不传此参数即选择全部。

```powershell
# Windows：安装韩立（Han Li）
py -3 scripts/install.py --pet hanli-2
# Windows：安装二嘟（Erdu）、韩立（Han Li）和 CC猫（CC Mao）
py -3 scripts/install.py --pet erdu --pet hanli-2 --pet cc-cat-3
```

```sh
# macOS / Linux：安装韩立（Han Li）
python3 scripts/install.py --pet hanli-2
# macOS / Linux：安装二嘟（Erdu）、韩立（Han Li）和 CC猫（CC Mao）
python3 scripts/install.py --pet erdu --pet hanli-2 --pet cc-cat-3
```

可选 slug 的完整列表见[合集目录](../README.md)。重复指定同一只不会重复安装。
任意安装命令都可增加 `--dry-run`，例如 `py -3 scripts/install.py --pet erdu --dry-run`。

## 5. 目标目录与 CODEX_HOME

| 设置 | 安装根目录 |
| --- | --- |
| 未设置 `CODEX_HOME` | 当前用户主目录下的 `.codex/pets/` |
| 已设置 `CODEX_HOME` | `CODEX_HOME` 指向的目录下的 `pets/` |
| 指定 `--dest` | 直接使用该参数指定的目录，优先于上述设置 |

Windows 默认通常是 `C:\Users\<用户名>\.codex\pets\`；macOS / Linux 默认是 `~/.codex/pets/`。
每只桌宠再按其原始 id 建立子目录。`--dest` 应指向 **pets 根目录**，无需附加某只桌宠的 id。

以下命令将一只桌宠安装到独立测试目录：

```powershell
py -3 scripts/install.py --pet erdu --dest "$env:USERPROFILE\codex-pets-test"
```

```sh
python3 scripts/install.py --pet erdu --dest "$HOME/codex-pets-test"
```

测试目录不会自动被客户端加载。正式使用时，应让安装路径与客户端实际使用的配置目录一致。
如需自定义 `CODEX_HOME`，可以先在当前终端中预览目标：

```powershell
$env:CODEX_HOME = "D:\CodexData"
py -3 scripts/install.py --dry-run
```

```sh
CODEX_HOME="$HOME/.codex-custom" python3 scripts/install.py --dry-run
```

这些示例不会替你更改客户端的配置目录。
安装器拒绝仓库内部、文件系统根目录，以及包含符号链接或 Windows junction 的路径；请使用普通目录。

## 6. 手动安装单只桌宠

不使用 Python 安装器时，可以手动复制；建议先运行完整性校验。
以韩立（Han Li）为例，仓库 slug 是 `hanli-2`，而 `pet.json` 内的 id 是 `hanli`：

1. 在仓库打开 `pets/hanli-2/`，确认其中有 `pet.json` 和 `spritesheet.webp`。
2. 找到客户端使用的 pets 根目录；默认是 `~/.codex/pets/`，自定义位置见上一节。
3. 如果目标已存在 `hanli` 文件夹，先按下一节处理冲突，不直接覆盖。
4. 在 pets 根目录下建立 `hanli` 文件夹，把上述两个文件直接放入其中。

正确层级如下；不要额外嵌套 `hanli-2` 或第二层 `pets`：

```text
.codex/
└── pets/
    └── hanli/
        ├── pet.json
        └── spritesheet.webp
```

另外两处名称映射是 `cc-cat-3 → cc-cat`、`yinyue-3 → yinyue`。
其他桌宠同样以 `pet.json` 中的 id 作为安装目录名，保留文件名和配置内容。
安装完成后重新打开客户端，在其桌宠选择界面选择宠物；具体入口以客户端版本为准。
安装脚本不会自动更改当前选中的宠物。

## 7. 已有文件、更新与冲突

| 输出 | 含义 |
| --- | --- |
| `INSTALLED` | 已创建新目录并写入这只桌宠 |
| `SKIP` | 目标目录恰好包含两个相同文件，无需重复安装 |
| `CONFLICT` | 目标内容不同、包含额外文件或不是普通目录，保留已有内容 |
| `WOULD INSTALL` | dry-run 预览，尚未写入 |

安装器不会覆盖冲突，也没有 `--force`。某只发生冲突时，其他符合条件的桌宠仍可安装。
例如把备份文件留在某只宠物目录里，也会被视为冲突。

更新仓库时，可在没有待保留本地改动的 Git 工作区运行 `git pull --ff-only`；ZIP 用户重新下载并解压到新文件夹。
然后重新运行校验与 `--dry-run`。只有内容相同的已安装版本会自动跳过；不同版本需要手动处理：

1. 关闭客户端，确认冲突报告中的具体 id 与实际目标路径。
2. 将该 id 的整个文件夹复制到 **pets 根目录以外**，例如个人备份目录；检查两个文件均已备份。
3. 确认备份后，将旧 id 文件夹移出 pets 根目录，使原目标位置空出。不要将它改名后留在 pets 内。
4. 重新运行该只桌宠的安装命令，再打开客户端检查。需要恢复时，将新目录移出，再移回备份。

备份、移动和恢复由你主动进行；脚本不会执行这些操作。

### 退出码

| 退出码 | 含义 |
| --- | --- |
| `0` | 校验成功，或安装 / dry-run 完成且没有冲突；相同文件跳过也算成功 |
| `1` | 校验、路径或文件读写失败，详情见错误信息 |
| `2` | 安装遇到冲突；命令行参数格式错误也可能由参数解析器返回 `2` |

Windows PowerShell 运行后用 `$LASTEXITCODE` 查看；macOS / Linux 用 `echo $?`。
校验器正常返回 `0` 或 `1`。安装出错后先查看输出，不要假定所有桌宠都未写入或都已安装。

## 8. 卸载

关闭客户端，核对要卸载的 **原始 id**，只移除 pets 根目录下对应的那个文件夹，再重新打开客户端。
例如韩立（Han Li）对应 `hanli`，不是仓库中的 `hanli-2`。如需保留，先将该文件夹备份到 pets 外。
不要删除整个 `.codex` 或整个 `pets` 目录；本仓库没有自动卸载命令，也不会代你删除已安装文件。

## 9. 常见问题

**找不到 Python 或提示版本过低。** 安装 Python 3.9+ 并重开终端；Windows 检查 `py -3 --version`，macOS / Linux 检查 `python3 --version`。

**校验失败。** 根据输出定位文件，重新完整下载仓库后重试。不要修改 `catalog.json` 的哈希来绕过错误；源文件夹也不应混入备份或额外桌宠。

**安装成功但客户端未显示。** 确认客户端支持自定义桌宠、使用了同一用户和同一 `CODEX_HOME`，再检查 `<pets根目录>/<id>/pet.json` 的层级并重开客户端。独立测试目录不会自动显示。

**银月狐狸显示了两个相同名字。** `yinyue-fox` 和 `yinyue-3` 是两个不同外观，原始显示名都可能是“银月狐狸”；安装 id 分别为 `yinyue-fox` 和 `yinyue`，可按预览图区分。

**客户端没有显示文档里的中文名。** 合集使用二嘟（Erdu）、财财（Caicai）、咕噜（Gulu）作为展示名；客户端仍读取原始 `pet.json` 的 `displayName`，可能显示 `erdu`、`caicai`、`gulu`。文档命名不会修改配置或安装 id。

**预览 GIF 和实际动作不完全相同。** 仓库 GIF 用于快速浏览；实际动作和播放速度由客户端读取精灵图后决定。

## 10. 通过 Petdex 安装

也可通过 [Petdex 官方文档](https://petdex.dev/docs) 介绍的客户端或 CLI 安装。已具备 Node.js / npm 环境时，官方 CLI 示例为：

```sh
npx petdex install erdu
```

这是独立的 Petdex 安装流程，会使用网络，不调用本仓库的 Python 安装器。
其目录、支持平台和覆盖行为以 Petdex 官方文档为准，不套用本页的 Python 安装器规则。

[返回合集](../README.md) · [English](INSTALL.en.md)
