PYTHON CONFIGURATION TIPS
=============================



## ANACONDA

1. 下载地址：https://www.anaconda.com/download/

2. 更新所有packages

        conda update --all

    如果遇到 ipykernel 也要更新的情况下可能会报错，这时先

        conda update ipykernel

    再 --all 即可

3. 升级 python

        conda install -c anaconda python=X.X

    （将 X.X 换成所需版本），之后运行

        conda update --all

3. 如果需要非 Anaconda 默认版本的其他环境，如更低或更高的版本，可以通过配置环境的形式来进行，参见 [Managing Python](https://conda.io/docs/user-guide/tasks/manage-python.html)

4. 清理过期的pkgs

        conda clean -t  # 清除 tar 包
    
        conda clean -p  # 清除 module 包
    
        conda clean -a  # 清除 tar 包和 module 包

-------------



## JUPYTER NOTEBOOK

1. 创建个性化配置文件

        jupyter notebook --generate-config

2. 确认kernel路径

        jupyter kernelspec list
    
        打开输出的路径，如果有 kernel.json 文件，则更改 argv 里的 python.exe 的路径到正确路径
    
        一般为 ~\Anaconda\python.exe

3. Windows下，打开
   
        C:\Documents and Settings\<username>\.jupyter\jupyter_notebook_config.py
    
        或者
    
        C:\users\<username>\.jupyter\jupyter_notebook_config.py

4. Jupyter 4.1 以上

        c.NotebookApp.notebook_dir = u'F:\\lab\\'     # working directory for self-defined packages
        c.FileContentsManager.root_dir = u'F:\\lab\\notebooks'    # default directory for notebooks
    
        # 注：如果Notebook存储路径中有与工作路径下同名的文件夹（大小写不敏感），则会自动切换工作路径

5. 更改 notebook 样式

        新建 ~\.jupyter\custom\custom.css，挑选 src 文件下合适主题，将代码复制过去

6. 默认显示行号和使用SublimeText的快捷键

        新建 ~\.jupyter\custom\custom.js，将 src/custom.js 的代码复制过去

7. 输出渲染

        一般渲染成 html 效果都很好，但是渲染成 pdf 由于 jupyter 调用的是 latex，经常出错。为了让内嵌图片和 Mathjax 公式更好的显示，探索出来的一套方法如下：

        > jupyter nbconvert "XXXX.ipynb"   # 渲染 html

        浏览器打开 XXXX.html，等 Mathjax 加载完成后“另存网页为 - 全部（.htm, .html)”，一般会存下来一个 XXXX.htm 文件和一个文件夹 XXXX_files

        安装 [wkhtmltopdf](https://wkhtmltopdf.org/)，有需要的话添加环境变量

        > wkhtmltopdf --allow "..\XXXX_files" "XXXX.htm" XXXX.pdf

        即可获得品质较高的 pdf 文件

--------



## MATPLOTLIB

1. 下载 Microsoft Yahei Mono （见同文件夹）

2. 解决 matplotlib 及 seaborn 中文显示问题

**matplotlib 3.3+:**

    - 打开：

            ~\Anaconda3\Lib\site-packages\matplotlib\mpl-data\matplotlibrc

    - 在 `#font.sans-serif` 列表中加入 Microsoft YaHei Mono

**older version:**

    - 打开：

            ~\Anaconda3\pkgs\<matplotlib>\Lib\site-packages\matplotlib\rcsetup.py (Anaconda 5+)
    
            ~\Anaconda3\Lib\site-packages\matplotlib\rcsetup.py (lower version)

    - 在 defaultParams['font.sans-serif'] 里加入 "Microsoft YaHei Mono"

**检查及debug**

    - 此时在 jupyter notebook 中执行 %pylab inline 之后，pylab.rcParams['font.sans-serif'] 中应当带有"Microsoft YaHei Mono"

    - 检查 C:\~\<username>\.matplotlib，如有fontList.py3k.cache文件，删除，并重新启动jupyter notebook

--------



## CVXOPT

1. 下载cvxopt的whl文件: http://www.lfd.uci.edu/~gohlke/pythonlibs/#cvxopt

2. 如果 pip install <cvxopt.whl> 出错，则先安装 [numpy+mkl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)

--------



## ORTOOLS

1. 下载[Google Ortools](https://developers.google.com/optimization/)

2. 解压, python setup.py install

--------



## OTHER PKGS

- conda install selenium

- conda install termcolor

- conda install gmpy2

- jupyter notebook autoreload 报错处理：

        # ~anaconda/Lib/importlib/__init__.py 中 reload() 函数
        # 加入一句判断，即最后一个 try 模块的末尾改成这样：
    
        spec = module.__spec__ = _bootstrap._find_spec(name, pkgpath, target)
        if spec:
            _bootstrap._exec(spec, module)
        return sys.modules[name]
