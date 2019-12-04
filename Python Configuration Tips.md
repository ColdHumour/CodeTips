PYTHON CONFIGURATION TIPS
=============================

## ANACONDA

1. 下载地址：https://www.anaconda.com/download/

2. 更新所有packages

        conda update --all

    如果遇到 ipykernel 也要更新的情况下可能会报错，这时先

        conda update ipykernel

    再 -all 即可

3. 目前安装的 Anaconda 默认 Python 3.6，如果要 3.5 或其他版本，则通过配置环境的形式来进行，参见 [Managing Python](https://conda.io/docs/user-guide/tasks/manage-python.html)

4. 清理过期的pkgs

        conda clean -t  # 清除tar包

        conda clean -p  # 清除包

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

        # 注：如果Notebook存储路径中有与工作路径下同名的文件夹（大小写不敏感），则会自动切换工作路径

5. 更改notebook样式

        新建 ~\.jupyter\custom\custom.css，挑选src文件下合适主题，将代码复制过去

6. 默认显示行号和使用SublimeText的快捷键

        新建 ~\.jupyter\custom\custom.js，将src/custom.js的代码复制过去

--------

## CVXOPT

1. 下载cvxopt的whl文件: http://www.lfd.uci.edu/~gohlke/pythonlibs/#cvxopt

2. 如果 pip install <cvxopt.whl> 出错，则先安装 [numpy+mkl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)

--------

## ORTOOLS

1. 下载[Google Ortools](https://developers.google.com/optimization/)

2. 解压, python setup.py install

--------

## gmpy2

1. 下载[gmpy2](https://github.com/aleaxit/gmpy/releases)

2. pip install ~.whl

--------

## MATPLOTLIB

1. 下载 Microsoft Yahei Mono （见同文件夹）

2. 解决matplotlib中文显示

    - 打开：

            ~\Anaconda3\pkgs\<matplotlib>\Lib\site-packages\matplotlib\rcsetup.py (Anaconda 5+)

            ~\Anaconda3\Lib\site-packages\matplotlib\rcsetup.py (lower version)

    - 在 defaultParams['font.sans-serif'] 里加入 "Microsoft YaHei Mono"

    - 此时在 jupyter notebook 中执行 %pylab inline 之后，pylab.rcParams['font.sans-serif'] 中应当带有"Microsoft YaHei Mono"

    - 检查 C:\~\<username>\.matplotlib，如有fontList.py3k.cache文件，删除，并重新启动jupyter notebook

3. 解决seaborn中文显示

    - 打开：

            ~\Anaconda3\pkgs\<seaborn>\Lib\site-packages\seaborn\rcmod.py (Anaconda 5+)

            ~\Anaconda3\Lib\site-packages\seaborn\rcmod.py (lower version)

    - 在 style_dict['font.sans-serif'] 里加入 "Microsoft YaHei Mono"

    - 此时在 jupyter notebook 中执行 %pylab inline 并 import seaborn 之后，pylab.rcParams['font.sans-serif'] 中应当带有"Microsoft YaHei Mono"

--------

## OTHER PKGS

- pip install selenium

- pip install termcolor

- jupyter notebook autoreload 报错处理：

        # ~anaconda/Lib/importlib/__init__.py 中 reload() 函数
        # 加入一句判断，即最后一个 try 模块的末尾改成这样：

        spec = module.__spec__ = _bootstrap._find_spec(name, pkgpath, target)
        if spec:
            _bootstrap._exec(spec, module)
        return sys.modules[name]
