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

--------



## CVXOPT

1. 下载 cvxopt 的 whl 文件: http://www.lfd.uci.edu/~gohlke/pythonlibs/#cvxopt

2. 如果 pip install <cvxopt.whl> 出错，则先安装 [numpy+mkl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)

--------



## OTHER PKGS

- conda install selenium

- conda install termcolor

- conda install plotly

- conda install gmpy2

- python -m pip install --user ortools
