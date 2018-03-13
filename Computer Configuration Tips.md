COMPUTER CONFIGURATION TIPS
=============================

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

2. 必装package

    (1) tomorrow

    (2) SublimeLinter-pycodestyle （需要先 pip install pylint）

        - ignore line too long:

            Preference - Package Settings - SublimeLinter - Settings

            "linters": {
                "pycodestyle": {
                    "ignore": ["E501"]
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

3. 常用配置

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
              height: 30px;
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

---

SQL
-------------

1. Navicat
    
    (1) https://navicat.com/en
