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
                            "R0912", "R0914", "R0913", "W0141", "R0902",
                            "R0201", "W0232"]
            }

3. 字体

    (1) 下载安装 Microsoft Yahei Mono

    (2) preference - settings-user:

            "font_size": 14,
            "font_face": "Microsoft Yahei Mono",

Ipython Notebook
------------------

1. 创建个性化配置文件

        ipython profile create

2. Windows下，打开
    
        C:\Documents and Settings\<username>\.ipython\profile_default\ipython_notebook_config.py

        或者

        C:\users\<username>\.ipython\profile_default\ipython_notebook_config.py

3. Ipython 2.x

        c.NotebookApp.notebook_dir = u'F:\\lab'                  # 工作路径
        c.FileNotebookManager.notebook_dir = u'F:\\lab\\ipython' # Notebook存储路径

4. Ipython 3.x

        c.NotebookApp.notebook_dir = u'D:\\lab'              # 工作路径
        c.FileContentsManager.root_dir = u'D:\\lab\\ipython' # Notebook存储路径

5. 更改notebook样式

        打开 ~\.ipython\profile_default\static\custom\custom.css，改成以下代码：

        /* 需要先装 Microsoft Yahei Mono 字体，否则把 font-family 改成其他名字 */
        div#notebook, div.CodeMirror, div.output_area pre, .highlight pre, div.output_wrapper, div.prompt {
          font-family: 'Microsoft Yahei Mono', Monaco, Lucida, Courier, monospace !important;
        }

        /* GLOBALS */
        body {background-color: #eff1f5;}
        a {color: #8fa1b3;}

        /* INTRO PAGE */
        .toolbar_info, .list-container {color: #1c3657;}

        /* NOTEBOOK */

        /* comment out this line to bring the toolbar back */
        /* div#maintoolbar, div#header {display: none !important;} */

        div#notebook {border-top: none;}

        div.input_prompt {color: #c59820;}
        div.output_prompt {color: #c98344;}
        div.input_area {
          border-radius: 0px;
          border: 1px solid #9ea7a6;
        }
        div.output_area pre {font-weight: normal; color: #2a343a;}
        div.output_subarea {font-weight: normal; color: #2a343a;}

        .rendered_html table, .rendered_html th, .rendered_html tr, .rendered_html td {
          border: 1px  #3f4944 solid;
          color: #3f4944;
        }
        div.output_html { font-family: 'Microsoft Yahei Mono'; }
        table.dataframe tr {border: 1px #2a343a;}

        div.cell.selected {border-radius: 0px;}
        div.cell.edit_mode {border-radius: 0px; border: thin solid #c98344;}
        div.text_cell_render, div.output_html {color: #2a343a;}

        span.ansiblack {color: #1c3657;}
        span.ansiblue {color: #b02f30;}
        span.ansigray {color: #84898c;}
        span.ansigreen {color: #237986;}
        span.ansipurple {color: #c59820;}
        span.ansired {color: #2a5491;}
        span.ansiyellow {color: #a03b1e;}

        div.output_stderr {background-color: #2a5491;}
        div.output_stderr pre {color: #a7cfa3;}

        .cm-s-ipython.CodeMirror {background: #eff1f5; color: #1c3657;}
        .cm-s-ipython div.CodeMirror-selected {background: #a7cfa3 !important;}
        .cm-s-ipython .CodeMirror-gutters {background: #b5d8f6; border-right: 0px;}
        .cm-s-ipython .CodeMirror-linenumber {color: #84898c;}
        .cm-s-ipython .CodeMirror-cursor {border-left: 1px solid #3f4944 !important;}

        .cm-s-ipython span.cm-comment {color: #c98344;}
        .cm-s-ipython span.cm-atom {color: #c59820;}
        .cm-s-ipython span.cm-number {color: #c59820;}

        .cm-s-ipython span.cm-property, .cm-s-ipython span.cm-attribute {color: #237986;}
        .cm-s-ipython span.cm-keyword {color: #2a5491;}
        .cm-s-ipython span.cm-string {color: #a03b1e;}
        .cm-s-ipython span.cm-operator {color: #c98344;}
        .cm-s-ipython span.cm-builtin {color: #c59820;}

        .cm-s-ipython span.cm-variable {color: #237986;}
        .cm-s-ipython span.cm-variable-2 {color: #484d79;}
        .cm-s-ipython span.cm-def {color: #43820d;}
        .cm-s-ipython span.cm-error {background: #ff3333; color: #eff1f5;}
        .cm-s-ipython span.cm-bracket {color: #2a343a;}
        .cm-s-ipython span.cm-tag {color: #2a5491;}
        .cm-s-ipython span.cm-link {color: #c59820;}

        .cm-s-ipython .CodeMirror-matchingbracket { text-decoration: underline; color: #1c3657 !important;}

6. 默认显示行号

        打开 ~\.ipython\profile_default\static\custom\custom.js，在末尾添加以下代码：

        define([
            'base/js/namespace',
            'base/js/events'
            ], 
            function(IPython, events) {
                events.on("app_initialized.NotebookApp", 
                    function () {
                        IPython.Cell.options_default.cm_config.lineNumbers = true;
                    }
                );
            }
        );

7. 安装MathJax到本地。打开命令行，运行ipython，输入

        from IPython.external import mathjax; mathjax.install_mathjax()

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

Chrome
-------------

1. 必装扩展
    
    (1) SwitchyOmega

    (2) ARC Welder (Android模拟器)

        下载ARC Welder (https://chrome.google.com/webstore/detail/arc-welder/emfinbmielocnlhgmfkkmkngdoccbadn)

        下载ARChon Runtime (http://archon-runtime.github.io/)， 解压

        在Chrome扩展程序中用开发者模式载入ARChon Runtime

        地址栏敲入chrome://plugins/ 开启Native Client