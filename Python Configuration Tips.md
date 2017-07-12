PYTHON CONFIGURATION TIPS
=============================

## ANACONDA

1. 下载地址：https://www.continuum.io/downloads/

2. 更新所有packages

        conda update --all

-------------

## JUPYTER NOTEBOOK

1. 创建个性化配置文件

        jupyter notebook --generate-config

2. 确认kernel路径

        jupyter kernelspec list

        打开输出的路径，如果有kernel.json文件，则更改argv里的python.exe的路径到正确路径

        一般为~\Anaconda\python.exe

3. Windows下，打开
    
        C:\Documents and Settings\<username>\.jupyter\jupyter_notebook_config.py

        或者

        C:\users\<username>\.jupyter\jupyter_notebook_config.py

4. Jupyter 4.1

        c.NotebookApp.notebook_dir = u'F:\\lab\\'     # 工作路径
        c.FileContentsManager.root_dir = u'F:\\lab\\ipython'    # Notebook存储路径

5. 更改notebook样式

        新建 ~\.jupyter\custom\custom.css，添加以下代码：

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

6. 默认显示行号和使用SublimeText的快捷键

        新建 ~\.jupyter\custom\custom.js，添加以下代码：

        console.log('[CUSTOMIZATION] loading sublime custom.js');
        require(
            [
                "codemirror/keymap/sublime",
                "notebook/js/cell",
                "base/js/namespace"
            ],
            function(sublime_keymap, cell, IPython) {
                cell.Cell.options_default.cm_config.lineNumbers = true;
                cell.Cell.options_default.cm_config.keyMap = 'sublime';

                // 不修改Ctrl+Enter
                cell.Cell.options_default.cm_config.extraKeys['Cmd-Enter'] = function(){console.log('cmd-enter')};
                cell.Cell.options_default.cm_config.extraKeys['Ctrl-Enter'] = function(){console.log('ctrl-enter')};
                cell.Cell.options_default.cm_config.extraKeys['Shift-Enter'] = function(){};

                // 用空格代替tab
                cell.Cell.options_default.cm_config.extraKeys['Tab'] = function(cm){cm.replaceSelection("    " , "end");}

                // 设置已存在cell的格式
                var cells = IPython.notebook.get_cells();
                for (var cl=0; cl<cells.length; cl++) {
                    cells[cl].code_mirror.setOption('lineNumbers', true);
                    cells[cl].code_mirror.setOption('keyMap', 'sublime');
                    cells[cl].code_mirror.setOption('extraKeys',
                        {
                            "Cmd-Enter": function(){},
                            "Ctrl-Enter": function(){},
                            "Tab": function(cm){cm.replaceSelection("    " , "end");}
                        }
                    );            
                }
            }
        );

-------------

## CYTHON

0. 参考资料：

- http://cython.org/

- Cython: A Guide to Python Programmers


1. 编译器选择

- 首选 Microsoft Visual Studio

- 在没有的情况下，对Python2.7和3.2，可以下载 Microsoft Visual C++ Compiler for Python 2.7，网址为：http://www.microsoft.com/en-us/download/details.aspx?id=44266

    安装完成后，对 ~python\Lib\distutils\msvc9compiler.py 中的 find_vcvarsall() 进行修改，注释掉原代码，改为：

        def find_vcvarsall(version):
            username = "UserName"  # 注意更改为正确的名称
            productdir = "C:/Users/{}/AppData/Local/Programs/Common/Microsoft/Visual C++ for Python/9.0".format(username)
            vcvarsall = os.path.join(productdir, "vcvarsall.bat")
            if os.path.isfile(vcvarsall):
                return vcvarsall
            else:
                return None

- 对3.3及以上，详见：https://github.com/cython/cython/wiki/CythonExtensionsOnWindows

- 对64位3.5，安装Visual C++ Build Tools 2015，网址为http://go.microsoft.com/fwlink/?LinkId=691126


2. 编译及使用

- 直接编译
    
    保存到 xxx.pyx 文件里，然后同路径下构建 setup.py，内容为：

        from distutils.core import setup
        from distutils.extension import Extension
    
        from Cython.Build import cythonize

        setup(ext_modules=cythonize('xxx.pyx'))

    之后命令行运行：

        python setup.py build_ext -i --compiler=msvc

    编译完成后同路径下出现 xxx.pyd，即可直接如py文件一样 import

- 直接 import pyx 文件
    
        import pyximport
        _ = pyximport.install()

    之后即可直接如py文件一样 import

- jupyter notebook 直接使用Cython代码

    运行：

        %load_ext Cython

    而后直接使用magic syntax

        %%cython
        cdef ...

    运行即可在其他cell调用编译好的函数


3. 注意事项

- 运算过程中需要考虑溢出问题与变量转换问题

- Cython中的"/"作用于int时为Python3中的"//"


--------

## CVXOPT
    
1. 下载numpy+mkl的whl文件: http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
    
2. 下载cvxopt的whl文件: http://www.lfd.uci.edu/~gohlke/pythonlibs/#cvxopt

3. 按顺序 pip install ~.whl 即可

--------

## MATPLOTLIB

1. 下载 Microsoft Yahei Mono （见同文件夹）

2. 解决matplotlib中文显示

    - 打开 ~\Anaconda3\Lib\site-packages\matplotlib\rcsetup.py

    - 在 defaultParams['font.sans-serif'] 里加入 "Microsoft YaHei Mono"

    - 此时在 jupyter notebook 中执行 %pylab inline 之后，pylab.rcParams['font.sans-serif'] 中应当带有"Microsoft YaHei Mono"

3. 解决seaborn中文显示

    - 打开 ~\Anaconda3\Lib\site-packages\seaborn\rcmod.py

    - 在 style_dict['font.sans-serif'] 里加入 "Microsoft YaHei Mono"

    - 此时在 jupyter notebook 中执行 %pylab inline 并 import seaborn 之后，pylab.rcParams['font.sans-serif'] 中应当带有"Microsoft YaHei Mono"

--------

## ORTOOLS

1. 下载[Google Ortools](https://developers.google.com/optimization/)

2. 解压, python setup.py install
