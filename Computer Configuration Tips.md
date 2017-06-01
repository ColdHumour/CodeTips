COMPUTER CONFIGURATION TIPS
=============================

Sublime Text
----------------

1. 触发package controller

    (1) 按 Ctrl + ` 调出console

    (2) 粘贴以下代码到底部命令行并回车：
        
            # ST3
            import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())

            # ST2
            import urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp) if not os.path.exists(ipp) else None;open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())

    (3) 重启Sublime Text, Ctrl + Shift + P, install

2. 必装package

    (1) tomorrow

    (2) [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter-for-ST2) （需要先 pip install pylint）

    (3) [SublimeJEDI](https://github.com/srusskih/SublimeJEDI)

    (4) SublimeCodeIntel （和JEDI同时装可能有bug，只装JEDI一般就够了）

3. 字体

    (1) 下载安装 Microsoft Yahei Mono

    (2) preference - settings-user:

            "font_size": 14,
            "font_face": "Microsoft Yahei Mono",
    		"tab_size": 4,
    		"translate_tabs_to_spaces": true,
            "word_wrap": true,
            "word_wrap_column": 100,


命令行工具
---------------

1. ConEmu: Powerful command line management tool

    (1) https://www.fosshub.com/ConEmu.html

	(2) 个性化：

		settings - Main - Main console font - Microsoft Yahei Mono
		settings - Appearance - Generic - Single instance mode (check)
		settings - Appearance - Generic - Multiple consoles... (check)
		settings - Tab bar - Tabs(...) - Tabs on bottom (uncheck)
		settings - Tab bar - Tab templates (...) - Console: [%s]
		settings - Task bar - Taskbar buttons - Show overlay icon (uncheck)
		settings - Task bar - Taskbar buttons - Active console only (choose)

2. Gow: Light version of Cygwin

    (1) https://github.com/bmatzelle/gow


Firefox
------------

1. 必装扩展

    (1) FoxyProxy

    (2) Adblock

    (3) Stylish

            #main-menubar > menu {
              -moz-box-ordinal-group: 1 !important;
              font-size: 15px;}  /*选单列 */

            #main-menubar menu menupopup * {
              font-size: 15px;
            }


            #nav-bar {
              -moz-box-ordinal-group: 2 !important;
              font-size: 15px;
            }  /*导航列 */

            #PersonalToolbar {
              -moz-box-ordinal-group: 3 !important;
              font-size: 15px;
              height: 40px;
            }  /*书签列 */

            #personal-bookmarks .bookmark-item > .toolbarbutton-icon {
             margin-left:15px !important;
             padding:0px !important;
            }

            #TabsToolbar {
              -moz-box-ordinal-group: 4 !important;
              font-size: 15px;
              height: 40px;
            }  /*分页列 */

Chrome
-------------

1. 必装扩展
    
    (1) SwitchyOmega

    (2) ARC Welder (Android模拟器)

        下载ARC Welder (https://chrome.google.com/webstore/detail/arc-welder/emfinbmielocnlhgmfkkmkngdoccbadn)

        下载ARChon Runtime (http://archon-runtime.github.io/)， 解压

        在Chrome扩展程序中用开发者模式载入ARChon Runtime

        地址栏敲入chrome://plugins/ 开启Native Client
