# Dxlian 的桌宠合集 · Codex Pets

**简体中文** | [English](README.en.md)

15 只会动的小伙伴，来自 [@dxlian 的 Petdex 主页](https://petdex.dev/u/dxlian)：11 只《凡人修仙传》风格的同人角色与形态、3 只由 dxlian 原创的桌宠——二嘟（Erdu）、财财（Caicai）、咕噜（Gulu），以及表情包风格的 CC猫（CC Mao）。

这是桌宠**素材与安装工具合集**。每只包含原始 `pet.json` 和透明背景精灵图，供支持该格式的 Codex 桌面客户端使用；仓库本身不是一个独立运行的桌宠应用。Python 安装器可在 Windows、macOS、Linux 上运行，桌面客户端与自定义桌宠功能是否可用需以对应平台和版本为准。

**15 只桌宠 · 动态图鉴 · 中文 / English · 单只 / 批量安装 · SHA-256 校验**

- [下载完整合集 ZIP](https://github.com/dxlian/codex-pets/archive/refs/heads/main.zip)
- [详细安装说明（中文）](docs/INSTALL.zh-CN.md) · [Installation guide (English)](docs/INSTALL.en.md)
- [每只桌宠的介绍](#每只桌宠的介绍) · [完整编号对照](#完整编号对照) · [文件与版本](#文件与版本)

## 动态图鉴

点击名字打开 Petdex 页面，点击「素材」查看完整文件。GIF 来自网站公开预览帧，每只包含 6 帧循环；它用于展示外观，并不代表客户端中的全部动作或实际播放速度。

<table>
<tr>
<td align="center" width="33%"><a href="https://petdex.dev/pets/erdu"><img src="previews/erdu.gif" width="192" height="208" alt="二嘟（Erdu） 动态预览"><br><b>二嘟（Erdu）</b></a><br><a href="pets/erdu">素材</a> · <code>erdu</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/hanli-2"><img src="previews/hanli-2.gif" width="192" height="208" alt="韩立（Han Li） 动态预览"><br><b>韩立（Han Li）</b></a><br><a href="pets/hanli-2">素材</a> · <code>hanli-2</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/yinyue-yitong"><img src="previews/yinyue-yitong.gif" width="192" height="208" alt="银月·异瞳（Yinyue Yitong） 动态预览"><br><b>银月·异瞳（Yinyue Yitong）</b></a><br><a href="pets/yinyue-yitong">素材</a> · <code>yinyue-yitong</code></td>
</tr>
<tr>
<td align="center" width="33%"><a href="https://petdex.dev/pets/xuangu"><img src="previews/xuangu.gif" width="192" height="208" alt="玄骨（Xuangu） 动态预览"><br><b>玄骨（Xuangu）</b></a><br><a href="pets/xuangu">素材</a> · <code>xuangu</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/song-yu"><img src="previews/song-yu.gif" width="192" height="208" alt="宋玉（Song Yu） 动态预览"><br><b>宋玉（Song Yu）</b></a><br><a href="pets/song-yu">素材</a> · <code>song-yu</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/wang-chan-wheelchair"><img src="previews/wang-chan-wheelchair.gif" width="192" height="208" alt="王婵（Wang Chan） 动态预览"><br><b>王婵（Wang Chan）</b></a><br><a href="pets/wang-chan-wheelchair">素材</a> · <code>wang-chan-wheelchair</code></td>
</tr>
<tr>
<td align="center" width="33%"><a href="https://petdex.dev/pets/fengxi"><img src="previews/fengxi.gif" width="192" height="208" alt="风希（Fengxi） 动态预览"><br><b>风希（Fengxi）</b></a><br><a href="pets/fengxi">素材</a> · <code>fengxi</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/nanlonghou"><img src="previews/nanlonghou.gif" width="192" height="208" alt="南陇候（Nanlonghou） 动态预览"><br><b>南陇候（Nanlonghou）</b></a><br><a href="pets/nanlonghou">素材</a> · <code>nanlonghou</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/yinyue-fox"><img src="previews/yinyue-fox.gif" width="192" height="208" alt="银月狐狸·深耳版（Yinyue Huli Shen&#x27;er Ban） 动态预览"><br><b>银月狐狸·深耳版（Yinyue Huli Shen&#x27;er Ban）</b></a><br><a href="pets/yinyue-fox">素材</a> · <code>yinyue-fox</code></td>
</tr>
<tr>
<td align="center" width="33%"><a href="https://petdex.dev/pets/wen-tianren"><img src="previews/wen-tianren.gif" width="192" height="208" alt="温天仁（Wen Tianren） 动态预览"><br><b>温天仁（Wen Tianren）</b></a><br><a href="pets/wen-tianren">素材</a> · <code>wen-tianren</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/yinyue-3"><img src="previews/yinyue-3.gif" width="192" height="208" alt="银月狐狸·蓝耳版（Yinyue Huli Lan&#x27;er Ban） 动态预览"><br><b>银月狐狸·蓝耳版（Yinyue Huli Lan&#x27;er Ban）</b></a><br><a href="pets/yinyue-3">素材</a> · <code>yinyue-3</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/ziling"><img src="previews/ziling.gif" width="192" height="208" alt="紫灵（Ziling） 动态预览"><br><b>紫灵（Ziling）</b></a><br><a href="pets/ziling">素材</a> · <code>ziling</code></td>
</tr>
<tr>
<td align="center" width="33%"><a href="https://petdex.dev/pets/caicai"><img src="previews/caicai.gif" width="192" height="208" alt="财财（Caicai） 动态预览"><br><b>财财（Caicai）</b></a><br><a href="pets/caicai">素材</a> · <code>caicai</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/cc-cat-3"><img src="previews/cc-cat-3.gif" width="192" height="208" alt="CC猫（CC Mao） 动态预览"><br><b>CC猫（CC Mao）</b></a><br><a href="pets/cc-cat-3">素材</a> · <code>cc-cat-3</code></td>
<td align="center" width="33%"><a href="https://petdex.dev/pets/gulu"><img src="previews/gulu.gif" width="192" height="208" alt="咕噜（Gulu） 动态预览"><br><b>咕噜（Gulu）</b></a><br><a href="pets/gulu">素材</a> · <code>gulu</code></td>
</tr>
</table>

## 快速安装

需要 **Python 3.9 或更高版本**；安装器仅使用标准库，无需 `pip install`。也可以按[手动安装说明](docs/INSTALL.zh-CN.md#6-手动安装单只桌宠)复制两份素材文件。

### 1. 获取文件

下载并解压上方 ZIP，在解压后的 `codex-pets-main` 文件夹打开终端；也可以通过 Git 获取：

```sh
git clone https://github.com/dxlian/codex-pets.git
cd codex-pets
```

运行以下命令时，当前目录应当能看到 `README.md`、`catalog.json`、`pets/` 和 `scripts/`。

### 2. 检查并安装

Windows PowerShell：

```powershell
py -3 --version
py -3 scripts/validate.py
py -3 scripts/install.py --dry-run
py -3 scripts/install.py
```

macOS / Linux 终端：

```sh
python3 --version
python3 scripts/validate.py
python3 scripts/install.py --dry-run
python3 scripts/install.py
```

只装指定桌宠时，在安装命令中加上 `--pet`，可重复选择多只。例如 Windows：

```powershell
py -3 scripts/install.py --pet erdu --pet caicai --pet gulu
```

macOS / Linux 将 `py -3` 替换为 `python3`。完整参数、指定安装目录、无需 Python 的手动安装、更新、卸载和常见问题见[详细安装说明](docs/INSTALL.zh-CN.md)。

### 3. 在客户端中选择

默认安装到 `~/.codex/pets/<原始 id>/`；如果设置了 `CODEX_HOME`，则安装到 `$CODEX_HOME/pets/<原始 id>/`。重新打开支持自定义桌宠的 Codex 桌面客户端，在其桌宠选择界面中选中需要的角色。安装器不会自动更改当前选择。

相同文件会跳过，遇到不同版本会报告 `CONFLICT` 并保留现有文件。无需管理员权限，也不会通过网络下载其他内容。

### 使用 Petdex 桌面端

也可以前往每只桌宠的 Petdex 页面，按网站提供的方式安装，或使用官方 CLI：

```sh
npx petdex install erdu
```

这条命令需要 Node.js / npm，并按 Petdex 自身的流程安装；它与仓库中写入 Codex 目录的离线 Python 安装器不同。目录与客户端行为以 [Petdex 官方文档](https://petdex.dev/docs) 为准。

## 每只桌宠的介绍

以下介绍依据原始发布说明与图像外观整理。全部收录的 Petdex 精灵版本均为 **v1**。中英文文档统一采用“中文名（拼音）”作为展示名称；原始 `pet.json` 的 `displayName` 和 id 保持不变，客户端因此可能仍显示发布时的原名。

下面逐只安装命令中的 `python`，Windows 可替换为 `py -3`，macOS / Linux 可替换为 `python3`。

### 01. 二嘟（Erdu）

**原创桌宠 · 作者：dxlian**

一只比熊犬风格的白色毛茸茸小狗：圆黑眼睛、软软的垂耳、黑色纽扣鼻，以及伸出一点点的小舌头。整体轮廓圆润，表情开心，适合喜欢温暖、轻松陪伴感的人。

[Petdex 页面](https://petdex.dev/pets/erdu) · [素材目录](pets/erdu) · 安装目录：`erdu`

```sh
python scripts/install.py --pet erdu
```

### 02. 韩立（Han Li）

身穿青蓝色长袍的 Q 版修仙者，背后的风雷翅是最醒目的设计标志。小巧的人物比例配上展开的羽翼，让这只桌宠同时保留修仙角色的装束和鲜明的轮廓。

[Petdex 页面](https://petdex.dev/pets/hanli-2) · [素材目录](pets/hanli-2) · 安装目录：`hanli`

```sh
python scripts/install.py --pet hanli-2
```

### 03. 银月·异瞳（Yinyue Yitong）

银发、狐耳与异色双瞳构成主要辨识点，白色衣装搭配红色腰带，整体气质清冷又带一点俏皮。这是银月的人形狐耳版本，与下面两只狐狸形态分别收录。

[Petdex 页面](https://petdex.dev/pets/yinyue-yitong) · [素材目录](pets/yinyue-yitong) · 安装目录：`yinyue-yitong`

```sh
python scripts/install.py --pet yinyue-yitong
```

### 04. 玄骨（Xuangu）

黑发蓝袍的魔道修仙者，带有红色眼部装饰、金色护喉与蓝色流苏耳饰。设计说明包含幽蓝火焰元素，整体表情冷峻；本合集保留 Petdex 已发布的玄骨版本。

[Petdex 页面](https://petdex.dev/pets/xuangu) · [素材目录](pets/xuangu) · 安装目录：`xuangu`

```sh
python scripts/install.py --pet xuangu
```

### 05. 宋玉（Song Yu）

以《凡人修仙传》宋玉为灵感的小型修仙桌宠，长发配白色、青绿色衣裙与发饰。线条和姿态偏柔和，呈现清雅、从容的仙侠风格。

[Petdex 页面](https://petdex.dev/pets/song-yu) · [素材目录](pets/song-yu) · 安装目录：`song-yu`

```sh
python scripts/install.py --pet song-yu
```

### 06. 王婵（Wang Chan）

采用坐在华丽青铜色轮椅中的造型，紫黑长袍、冷峻表情和轮椅结构构成鲜明特征。原始设计说明以血灵修炼姿态为动作意象，适合喜欢魔道角色与复杂服饰细节的人。

[Petdex 页面](https://petdex.dev/pets/wang-chan-wheelchair) · [素材目录](pets/wang-chan-wheelchair) · 安装目录：`wang-chan-wheelchair`

```sh
python scripts/install.py --pet wang-chan-wheelchair
```

### 07. 风希（Fengxi）

以较修长的成年人物比例呈现，头戴金冠，身着深蓝紫长袍，并配有银蓝兽形肩甲、獠牙状肩饰和青色腰部装饰。相比合集中的圆头 Q 版人物，这一版的轮廓更细长、气质更冷峻。

[Petdex 页面](https://petdex.dev/pets/fengxi) · [素材目录](pets/fengxi) · 安装目录：`fengxi`

```sh
python scripts/install.py --pet fengxi
```

### 08. 南陇候（Nanlonghou）

蓝金长袍与冠饰形成醒目的修仙者形象，整体采用 Q 版比例。原始设计说明以“万尺一线”遁光作为动作意象，视觉上突出蓝色衣装与金色装饰的搭配。

[Petdex 页面](https://petdex.dev/pets/nanlonghou) · [素材目录](pets/nanlonghou) · 安装目录：`nanlonghou`

```sh
python scripts/install.py --pet nanlonghou
```

### 09. 银月狐狸·深耳版（Yinyue Huli Shen'er Ban）

参考银月狐狸第二形态制作：白色绒毛、深色耳朵、杏仁形眼睛和蓬松卷尾，神态较为灵巧。这一版的安装 id 是 `yinyue-fox`，与蓝耳版 `yinyue` 不同，两只可以同时保留。

[Petdex 页面](https://petdex.dev/pets/yinyue-fox) · [素材目录](pets/yinyue-fox) · 安装目录：`yinyue-fox`

```sh
python scripts/install.py --pet yinyue-fox
```

### 10. 温天仁（Wen Tianren）

身穿紫金色服装的 Q 版修仙者，长发与冠饰强化了人物轮廓。整体呈现自信、略带傲气的角色气质，紫色与金色也是这只桌宠最直观的配色标志。

[Petdex 页面](https://petdex.dev/pets/wen-tianren) · [素材目录](pets/wen-tianren) · 安装目录：`wen-tianren`

```sh
python scripts/install.py --pet wen-tianren
```

### 11. 银月狐狸·蓝耳版（Yinyue Huli Lan'er Ban）

圆脸白色小狐狸，具有蓝色耳尖、蓝色额印、浅蓝脸纹、异色眼睛、黑色小鼻子和蓬松卷尾。Petdex 编号为 `yinyue-3`，原始安装 id 为 `yinyue`；它与深耳版的图片不同，并非重复文件。

[Petdex 页面](https://petdex.dev/pets/yinyue-3) · [素材目录](pets/yinyue-3) · 安装目录：`yinyue`

```sh
python scripts/install.py --pet yinyue-3
```

### 12. 紫灵（Ziling）

黑色长发、面纱、蓝紫色眼睛与白蓝长裙，搭配金色装饰，构成安静的修仙者形象。人物比例偏修长，面纱和衣裙细节体现了这只桌宠清雅、沉静的气质。

[Petdex 页面](https://petdex.dev/pets/ziling) · [素材目录](pets/ziling) · 安装目录：`ziling`

```sh
python scripts/install.py --pet ziling
```

### 13. 财财（Caicai）

**原创桌宠 · 作者：dxlian**

银白色长毛小猫，带有蓝灰色大眼睛、粉色鼻子、耳尖绒毛和蓬松胸毛。表情温柔、步态设计轻柔，适合偏爱安静小猫形象的人。

[Petdex 页面](https://petdex.dev/pets/caicai) · [素材目录](pets/caicai) · 安装目录：`caicai`

```sh
python scripts/install.py --pet caicai
```

### 14. CC猫（CC Mao）

奶油色的表情包风格小猫，宽圆的大脑袋、侧看的眼睛、红晕、胡须、夸张笑嘴与白色肚皮都很醒目。头大身小的比例和开心表情让它成为合集里偏轻松搞怪的一只。

[Petdex 页面](https://petdex.dev/pets/cc-cat-3) · [素材目录](pets/cc-cat-3) · 安装目录：`cc-cat`

```sh
python scripts/install.py --pet cc-cat-3
```

### 15. 咕噜（Gulu）

**原创桌宠 · 作者：dxlian**

圆润的银色虎斑猫，拥有绿色大眼睛、粉色鼻子、白色嘴边毛、深色额纹和柔和的灰色环状花纹。与长毛的财财相比，咕噜的辨识点是虎斑纹路和圆圆的脸。

[Petdex 页面](https://petdex.dev/pets/gulu) · [素材目录](pets/gulu) · 安装目录：`gulu`

```sh
python scripts/install.py --pet gulu
```

## 完整编号对照

`slug` 是 Petdex 页面编号、仓库文件夹名以及 `--pet` 参数；`id` 是原始 `pet.json` 里的编号，也是客户端安装文件夹名。韩立（Han Li）、CC猫（CC Mao） 和蓝耳版银月的二者不同，安装器会自动转换。

| 桌宠 | Petdex slug / 仓库目录 | 原始 id / 安装目录 |
| --- | --- | --- |
| [二嘟（Erdu）](https://petdex.dev/pets/erdu) | `erdu` | `erdu` |
| [韩立（Han Li）](https://petdex.dev/pets/hanli-2) | `hanli-2` | `hanli` |
| [银月·异瞳（Yinyue Yitong）](https://petdex.dev/pets/yinyue-yitong) | `yinyue-yitong` | `yinyue-yitong` |
| [玄骨（Xuangu）](https://petdex.dev/pets/xuangu) | `xuangu` | `xuangu` |
| [宋玉（Song Yu）](https://petdex.dev/pets/song-yu) | `song-yu` | `song-yu` |
| [王婵（Wang Chan）](https://petdex.dev/pets/wang-chan-wheelchair) | `wang-chan-wheelchair` | `wang-chan-wheelchair` |
| [风希（Fengxi）](https://petdex.dev/pets/fengxi) | `fengxi` | `fengxi` |
| [南陇候（Nanlonghou）](https://petdex.dev/pets/nanlonghou) | `nanlonghou` | `nanlonghou` |
| [银月狐狸·深耳版（Yinyue Huli Shen'er Ban）](https://petdex.dev/pets/yinyue-fox) | `yinyue-fox` | `yinyue-fox` |
| [温天仁（Wen Tianren）](https://petdex.dev/pets/wen-tianren) | `wen-tianren` | `wen-tianren` |
| [银月狐狸·蓝耳版（Yinyue Huli Lan'er Ban）](https://petdex.dev/pets/yinyue-3) | `yinyue-3` | `yinyue` |
| [紫灵（Ziling）](https://petdex.dev/pets/ziling) | `ziling` | `ziling` |
| [财财（Caicai）](https://petdex.dev/pets/caicai) | `caicai` | `caicai` |
| [CC猫（CC Mao）](https://petdex.dev/pets/cc-cat-3) | `cc-cat-3` | `cc-cat` |
| [咕噜（Gulu）](https://petdex.dev/pets/gulu) | `gulu` | `gulu` |

## 文件与版本

```text
README.md                    中文图鉴、简介与快速开始
README.en.md                 English gallery, profiles, and quick start
docs/INSTALL.zh-CN.md        详细中文安装与故障排查
docs/INSTALL.en.md           Detailed English installation guide
pets/<slug>/pet.json          桌宠原始名称、说明、id 和图片路径
pets/<slug>/spritesheet.webp  原始透明精灵图，1536 × 1872
previews/<slug>.gif           192 × 208 动态预览，每只 6 帧
catalog.json                 名录、来源、版本、字节数与 SHA-256
scripts/install.py           离线安装器
scripts/validate.py          完整性检查
```

## 来源与说明

- 桌宠发布者：[dxlian](https://github.com/dxlian) · [Petdex 主页](https://petdex.dev/u/dxlian)
- **原创作品：二嘟（Erdu）、财财（Caicai）、咕噜（Gulu）均为 dxlian 原创桌宠。**
- 展示与安装平台：[Petdex](https://petdex.dev) · [Petdex 开源项目](https://github.com/crafter-station/petdex)
- 与既有作品有关的桌宠属于同人创作，原作角色、名称及相关权利归各自权利人。本仓库整理不代表授予原作 IP 或美术素材的额外许可。

发现遗漏、文件问题或说明错误，可在 [Issues](https://github.com/dxlian/codex-pets/issues) 中反馈。提交问题时提供系统、Python 版本、使用的命令和错误信息即可，无需上传个人配置或凭据。
