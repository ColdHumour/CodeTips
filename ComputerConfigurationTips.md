COMPUTER CONFIGURATION TIPS
=============================

sublime text
----------------

1. 触发package controller

    (1) 按 Ctrl + ` 调出console

    (2) 粘贴以下代码到底部命令行并回车：
        
            import urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp) if not os.path.exists(ipp) else None;open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())

    (3) 重启Sublime Text 2, Ctrl + Shift + P, install

2. 必装package

    (1) tomorrow

    (2) pylinter （需要先 pip install pylint）

            Preferences - Package Settings - Pylinter - Settings User:

            {
                "disable": ["C0103", "C0111", "C0304", "W0231", "W0102", 
                            "R0903", "W0702", "W0613", "C0326", "R0901",
                            "C0330", "W0201", "W0212", "W0612", "E1121",
                            "W0621", "W0614", "C0321", "C0301", "R0915",
                            "R0912", "R0914", "R0913", "W0141", "R0902"]
            }

3. 字体

    (1) 下载安装 Microsoft Yahei Mono

    (2) preference - settings-user:

            "font_size": 14,
            "font_face": "Microsoft Yahei Mono",


Firefox
------------

1. 必装扩展

    (1) FoxyProxy

    (2) Adblock

    (3) Stylish

            #toolbar-menubar {-moz-box-ordinal-group: 1 !important;}  /*选单列 */
            #nav-bar {-moz-box-ordinal-group: 2 !important;}  /*导航列 */
            #PersonalToolbar {-moz-box-ordinal-group: 3 !important;}  /*书签列 */
            #TabsToolbar {-moz-box-ordinal-group: 4 !important;}  /*分页列 */
            #addon-bar {-moz-box-ordinal-group: 45 !important;}  /*fx28以下的附加组件栏 */
            
Ipython Notebook
------------------

1. 创建个性化配置文件

        ipython profile create

2. Windows下，打开
    
        Documents and Settings\username\.ipython\profile_default\ipython_notebook_config.py

3. Ipython 2.x

        c.NotebookApp.notebook_dir = u'F:\\lab'                  # 工作路径
        c.FileNotebookManager.notebook_dir = u'F:\\lab\\ipython' # Notebook存储路径

4. Ipython 3.x

        c.NotebookApp.notebook_dir = u'D:\\lab'              # 工作路径
        c.FileContentsManager.root_dir = u'D:\\lab\\ipython' # Notebook存储路径