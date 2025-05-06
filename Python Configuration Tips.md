PYTHON CONFIGURATION TIPS
=============================



## ANACONDA

1. 下载地址：https://www.anaconda.com/download/

2. 更新所有packages

        conda update --all

    如果遇到 ipykernel 也要更新的情况下可能会报错，这时先

        conda update ipykernel

    再 --all 即可

3. 升级 python 大版本（如 3.9 到 3.10）

        conda install -c anaconda python=X.X

    （将 X.X 换成所需版本），之后运行

        conda update --all

3. 如果需要非 Anaconda 默认版本的其他环境，如更低或更高的版本，可以通过配置环境的形式来进行，参见 [Managing Python](https://conda.io/docs/user-guide/tasks/manage-python.html)

4. 清理过期的pkgs

        conda clean -t  # 清除 tar 包
    
        conda clean -p  # 清除 module 包
    
        conda clean -a  # 清除 tar 包和 module 包

5. 锁定某些 pkgs 不升级（比如被坑过很多回的 plotly 不支持 ipywidgets 8.X）

    在 ~anaconda/conda-meta/pinned 文件中写入，示例格式

        numpy 1.7.X
        scipy ==0.14.2

6. 代理设置

    打开 \~/\<user\>/.condarc 输入

        proxy_servers: {
            http: <host>:<port>,
            https: <host>:<port>
        }

-------------


## JUPYTER NOTEBOOK

*版本7+*

1. 启动

        jupyter nbclassic

2. 创建个性化配置文件

        jupyter server --generate-config

3. 确认kernel路径

        jupyter kernelspec list
    
        打开输出的路径，如果有 kernel.json 文件，则更改 argv 里的 python.exe 的路径到正确路径
    
        一般为 ~\Anaconda\python.exe

4. Windows下，打开
   
        C:\Documents and Settings\<username>\.jupyter\jupyter_server_config.py
    
        或者
    
        C:\users\<username>\.jupyter\jupyter_server_config.py

在文件开头加入

        c.ServerApp.root_dir = u'F:\\lab\\'     # working directory for self-defined packages
        c.FileContentsManager.root_dir = u'F:\\lab\\notebooks'    # default directory for notebooks
    
        # 注：如果Notebook存储路径中有与工作路径下同名的文件夹（大小写不敏感），则会自动切换工作路径

5. 更改 notebook 样式

        新建 ~\.jupyter\custom\custom.css，挑选 src 文件下合适主题，将代码复制过去

6. 默认显示行号和使用SublimeText的快捷键

        新建 ~\.jupyter\custom\custom.js，将 src/custom.js 的代码复制过去

7. 自动换行

        新建 ~\.jupyter\nbconfig\notebook.json，将 src/notebook.json 的代码复制过去

8. 如果要打开两个 notebook 环境，建议创建另一个 config 文件，把相应参数修改好后

        jupyter server --config=".jupyter/new_config_file.py" --port=XXXX

9. Jupyter Notebook 界面语言调整

某个版本之后 notebook 界面交互语言会跟系统走，要锁定英文的话：

    - 打开 ~anaconda\Lib\site-packages\notebook\notebookapp.py

    - 找到 `nbui = gettext.translation` 所在行，在参数中加上 languages="eng"

10. Jupyter Notebook Autoreload

在 cell 中执行

        %load_ext autoreload
        %autoreload 2

可以自动重载编辑过的 py 文件，在用诸如 sublime text 等编辑器联调的时候很方便

但是有的时候 autoreload 会报 exception，不影响使用，但挺烦心的

使用如下方法使 autoreload 不报错

        # ~anaconda/Lib/importlib/__init__.py 中 reload() 函数
        # 加入一句判断，即最后一个 try 模块的末尾改成这样：
    
        spec = module.__spec__ = _bootstrap._find_spec(name, pkgpath, target)
        if spec:
            _bootstrap._exec(spec, module)
        return sys.modules[name]

---


## JUPYTER LAB

鉴于 Jupyter lab 目前还有一些影响使用的 bug，这里先把能解决的部分列出来，剩余的慢慢补充。

1. 主题

找到 `~anaconda\share\jupyter\lab\themes\index.css`，对照 custom.css 比较关键字调整字体、颜色等

2. Error `could not determine jupyterlab build status without Node.js`

        conda install -c conda-forge nodejs

3. Error `Could not determine npm prefix [WinError 2]`

找到 `~anaconda\Lib\site-packages\jupyter_lsp\types.py` 里的 `def _npm_prefix()` 方法，把 "npm" 改成 "npm.cmd"


---


## MATPLOTLIB 中文显示

下载 Microsoft Yahei Mono 并安装 （见 ./src）

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


## pandas 2.0 pickle/shelve 读取错误

在 `~/site-packages/pandas/core/indexes` 下创建 `numeric.py`：

        from pandas.core.indexes.base import Index

        class NumericIndex(Index):
            pass

        class IntegerIndex(NumericIndex):
            pass

        class Int64Index(IntegerIndex):
            pass

        class UInt64Index(IntegerIndex):
            pass

        class Float64Index(NumericIndex):
            pass

---


## pillow

1. `Import Error: DLL module cannot be loaded __imgaing` at `from PIL import Image`

    - 从 [pillow](https://pypi.org/project/pillow) 下载对应的 `.whl` 文件，例如 cp39-win_amd64

    - 从程序打开 Anaconda Powershell Prompt

    - pip install pillow~.whl

---

## gmpy2

- conda install gmpy2

- `DLL load failed while importing gmpy2`：从 [gmpy2](https://pypi.org/project/gmpy2) 下载对应的 `.whl` 文件，例如 cp39-win_amd64，然后参照上面


----


## OTHER PKGS

- conda install -c conda-forge cvxopt

- conda install -c conda-forge cvxpy

- conda install selenium

- conda install termcolor

- conda install gevent

- conda install arch -c bashtage

- conda install -c conda-forge pulp

- python -m pip install --user ortools  # 如果报 `ValueError: check_hostname requires server_hostname` 可以尝试在 .condarc 配置好 proxy_servers 后关闭系统代理，似乎 pip 会从配置的代理尝试连接故不用再设置系统代理
