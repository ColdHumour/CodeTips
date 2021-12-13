COMPUTER CONFIGURATION TIPS
=============================


## 权限问题

创建 bat 文件

        cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start "" %1"

将 exe 文件拖到 bat 文件上打开

---


## Firefox

#### 0. 下载并安装

- https://www.mozilla.org/en-US/firefox/new/

#### 1. 必装扩展

- **FoxyProxy**
- **Adblock**
- **FoxyTab**

#### 2. 经典界面还原

参考资料：
- https://github.com/Aris-t2/CustomCSSforFx
- https://www.userchrome.org/

(1) `about:support > Profile Folder > Open Folder`
        
or `Shift+F2` to open Firefox's command line, then enter the command: `folder openprofile`

(2) create folder: **chrome**

(3) copy **./src/userChrome.css** to such folder

(4) `about:config > toolkit.legacyUserProfileCustomizations.stylesheets > true`

#### 3. 多实例同时运行

- `"~/firefox.exe" -no-remote -ProfileManager`
- create new profile
- `"~/firefox.exe" -no-remote -P <new profile name>`

---



## Sublime Text 3

#### 0. 下载并安装

- https://www.sublimetext.com/3

#### 1. 配置 package controller

    点击  `Tools - Install Package Controller`，安装完成后该选项会消失

- 安装完成后重启 Sublime Text，`Ctrl + Shift + P`，输入 `install`

- 如需设置代理，进入 `Preferences - Package Settings - Package Control - Settings`，添加

```json
"http_proxy": "http://localhost:<port>",
"https_proxy": "http://localhost:<port>"
```

#### 2. 安装 package

(1) **tomorrow**

(2) **SublimeLinter** & **SublimeLinter-pycodestyle** （需要先 pip install pylint）

- disable specific messages:

    打开 `Preference - Package Settings - SublimeLinter - Settings`，添加

```json
{
    "lint_mode": "manual",
    "linters": {
        "pycodestyle": {
            "ignore": ["E501"]
        },
        "pylint": {
            "args": ["--disable=R0913,R0914,C0301"]
        }
    }
}
```

(3) **Jedi - Python autocompletion**

(4) **SideBarEnhancement**

(5) **A File Icon**

#### 3. 可选package

(1) **Anaconda**（只是个插件）

#### 4. 常用配置

(1) 下载安装 **Microsoft YaHei Mono**

(2) 打开 `Preferences - Settings`，修改为

```json
{
    "font_face": "Microsoft Yahei Mono",
    "font_size": 13,
    "ignored_packages":
    [
        "Vintage"
    ],
    "line_padding_bottom": 2,
    "line_padding_top": 2,
    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "word_wrap": true,
    "word_wrap_column": 100,
    "color_scheme": "Packages/Tomorrow Color Schemes/Tomorrow-Night.tmTheme",
}
```

#### 5. subl 启用方法

(1) 将 `~/<sublime text>/subl.exe` 复制到 `~/windows/system32` 下

(2) 在 cmd 下运行以下命令可使用 sublime text 打开文件或文件夹

```shell
subl <文件或文件夹路径>
```

(3) 其他选项见

```shell
subl --help
```

---



## Git

#### Git Bash

- 下载并安装：https://git-scm.com/download/win

#### GitKraken

- 下载并安装：https://www.gitkraken.com/
- 登录
- Preference - Authentication - 连接 Github 与 Bitbucket
- clone/open repository
- stage & commit & push

#### Git 代理设置

open `~/<user>/.gitconfig` and add following codes

```
[http]
    proxy = http://localhost:<port>
[https]
    proxy = https://localhost:<port>
```

### 局域网代码仓库设置

- 在局域网公共盘合适位置创建 XXXX.git 空文件夹
- 右键 Git Bash Here
- git --bare init --shared=group
- 完成之后就可以用 GitKraken 在本地 Clone 并 push 了


---



## ConEmu

- 下载并安装：https://conemu.github.io/

- 个性化：
    - settings - Fonts - Main console font - Microsoft Yahei Mono
    - settings - Appearance - Generic - Single instance mode (check)
    - settings - Appearance - Generic - Multiple consoles... (check)
    - settings - Tab bar - Tabs(...) - Tabs on bottom (uncheck)
    - settings - Tab bar - Tab templates (...) - Console: [%s]
    - settings - Task bar - Taskbar buttons - Show overlay icon (uncheck)
    - settings - Task bar - Taskbar buttons - Active console only (choose)

- 默认用 ConEmu 打开 .bat 或 .cmd
    - settings - Integration - Default term - Force ConEmu as default terminal for console applications (check)

- 解决中文乱码
    - settings - Startup - Environment 下方加入 `set LANG=zh_CN.UTF-8`，重启 ConEmu

---


### GOW

- 下载并安装：https://github.com/bmatzelle/gow

---



### Navicat

- Download: https://navicat.com/en

---
