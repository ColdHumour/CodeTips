COMPUTER CONFIGURATION TIPS
=============================

Git GUI For Windows
---------------------

GitKraken 和 GitHub Desktop 二选一即可，推荐 GitKraken，因可同时支持 GitHub 和 BitBucket，且可直接打开本地已 clone 的 repository

1. GitKraken

    - 下载：https://www.gitkraken.com/

    - 安装完成后使用 GitHub 登录

    - Preference - Authentication - Bitbucket.org 连接

    - clone/open repository

    - stage & commit & push

2. GitHub Desktop

    - https://desktop.github.com/

3. 代理设置

    - open ~/<user>/.gitconfig

    - add following codes:

        [http]
            proxy = http://<url>:<port>
        [https]
            proxy = https://<url>:<port>

---

Sublime Text
----------------

1. 触发 package controller

    - 方法一（初次安装时）：

        点击

            Tools - Install Package Controller

        安装完成后该选项会消失

    - 方法二：

        (1) View - Show Console 或者按 Ctrl + ` 调出console

        (2) 粘贴以下代码到底部命令行并回车：
        
            # ST3
            import urllib.request,os; pf = 'Package Control.sublime-package';
            ipp = sublime.installed_packages_path();
            urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler()));
            open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen('http://sublime.wbond.net/' + pf.replace(' ','%20')).read())

    - 安装完成后重启Sublime Text, Ctrl + Shift + P, install

    - 如需设置代理，进入 Preferences | Package Settings | Package Control | Settings - User，添加

            "http_proxy": "http://localhost:8888",
            "https_proxy": "http://localhost:8888"

2. 必装package

    (1) tomorrow

    (2) SublimeLinter & SublimeLinter-pycodestyle （需要先 pip install pylint）

        - disable specific messages:

            Preference - Package Settings - SublimeLinter - Settings

            {
                "lint_mode": "manual",
                "linters": {
                    "pycodestyle": {
                         "ignore": ["E501"]
                    }
                }
            }

    (3) Jedi - Python autocompletion

    (4) SideBarEnhancement

    (5) Boxy Theme 系列

        - Boxy Theme

        - Boxy Theme Addon - Font Face

        - A File Icon

3. 可选package：

    (1) SublimeCodeIntel （和JEDI同时装可能有bug，只装JEDI一般就够了）

4. 常用配置

    (1) 下载安装 Microsoft Yahei Mono

    (2) preference - settings-user:

            "color_scheme": "Packages/User/SublimeLinter/Tomorrow-Night (SL).tmTheme",
            "font_face": "Microsoft Yahei Mono",
            "font_size": 13,
            "ignored_packages":
            [
                "Vintage"
            ],
            "line_padding_bottom": 2,
            "line_padding_top": 2,
            "tab_size": 4,
            "theme": "Boxy Ocean.sublime-theme",
            "theme_sidebar_font_lg": true,
            "theme_sidebar_indent_xl": true,
            "translate_tabs_to_spaces": true,
            "word_wrap": true,
            "word_wrap_column": 100

5. Windows 命令行开启方法

    (1) 将 ~/sublime test 3/subl.exe 复制到 ~/windows/system32 下

    (2) 在命令行下运行以下命令可直接打开

            subl <文件或文件夹路径>

    (3) 其他选项见

            subl --help

---

命令行工具
---------------

1. ConEmu: Powerful command line management tool

    (1) https://conemu.github.io/

    (2) 个性化：

            settings - Main - Main console font - Microsoft Yahei Mono
            settings - Appearance - Generic - Single instance mode (check)
            settings - Appearance - Generic - Multiple consoles... (check)
            settings - Tab bar - Tabs(...) - Tabs on bottom (uncheck)
            settings - Tab bar - Tab templates (...) - Console: [%s]
            settings - Task bar - Taskbar buttons - Show overlay icon (uncheck)
            settings - Task bar - Taskbar buttons - Active console only (choose)

    (3) 默认用 ConEmu 打开 .bat 或 .cmd

            settings - Integration - Default term - Force ConEmu as default terminal for console applications (check)

2. Gow: Light version of Cygwin

    (1) https://github.com/bmatzelle/gow

---

Firefox
------------

1. 必装扩展

    (1) FoxyProxy

    (2) Adblock

2. 经典界面还原

    参考资料：https://github.com/Aris-t2/CustomCSSforFx

    (1) open profile folder

        about:support > Profile Folder > Open Folder

        Shift+F2 to open Firefox's command line, then enter the command: **folder openprofile**

    (2) create folder: chrome

    (3) create file: userChrome.css

            #main-menubar > menu {
              -moz-box-ordinal-group: 1 !important;
              font-size: 13px;}  /*选单列 */

            #main-menubar menu menupopup * {
              font-size: 13px;
            }

            #nav-bar {
              -moz-box-ordinal-group: 2 !important;
              font-size: 13px;
            }  /*导航列 */

            #PersonalToolbar {
              -moz-box-ordinal-group: 3 !important;
              font-size: 13px;
              height: 35px;
            }  /*书签列 */

            #personal-bookmarks .bookmark-item > .toolbarbutton-icon {
             margin-left: 10px !important;
             padding: 0px !important;
            }

            #TabsToolbar {
              -moz-box-ordinal-group: 4 !important;
              font-size: 13px;
              height: 30px;
            }  /*分页列 */

            #main-window:not([chromehidden*="toolbar"]) #navigator-toolbox {
              padding-bottom: 35px !important;
            }

            #TabsToolbar {
              position: absolute !important;
              bottom: 5px !important;
              width: 100vw !important;
            }

            #tabbrowser-tabs {
              width: 120vw !important;
            }

            /* hide line above navigation toolbar appearing in some cases */
            #main-window:not([tabsintitlebar]) #nav-bar,
            #main-window:not([tabsintitlebar]) #navigator-toolbox {
              border-top: 0 !important;
              box-shadow: unset !important;
            }

            /* disable Mozillas tab jumping nonsense when moving tabs */
            #navigator-toolbox[movingtab] > #titlebar > #TabsToolbar {
              padding-bottom: unset !important;
            }
            #navigator-toolbox[movingtab] #tabbrowser-tabs {
              padding-bottom: unset !important;
              margin-bottom: unset !important;
            }
            #navigator-toolbox[movingtab] > #nav-bar {
              margin-top: unset !important;
            }

            /* size of new tab tabs '+' icon */
            .tabs-newtab-button .toolbarbutton-icon {
              padding: 0px !important;
              margin: 0px !important;
              width: 15px !important;
              height: 15px !important;
            }

3. 多实例同时运行

    "~/firefox.exe" -no-remote -ProfileManager

    create new profile

    "~/firefox.exe" -no-remote -P <new profile name>

---

SQL
-------------

1. Navicat
    
    (1) https://navicat.com/en
