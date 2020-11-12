PYTHON TIPS
===============

主要用于记录各种疑难杂症的解决方案，免得重复劳动。

---

## Jupyter Notebook 输出渲染

转换成 html：

        > jupyter nbconvert --to html -template classic "XXXX.ipynb"   # 渲染 html

转换成 pdf，渲染图片和 mathjax：

        > 浏览器打开 XXXX.html，等 Mathjax 加载完成后“另存网页为 - 全部（.htm, .html)”，一般会存下来一个 XXXX.htm 文件和一个文件夹 XXXX_files

        安装 [wkhtmltopdf](https://wkhtmltopdf.org/)，有需要的话添加环境变量

        > wkhtmltopdf --allow "..\XXXX_files" "XXXX.htm" XXXX.pdf

        即可获得品质较高的 pdf 文件

---

## Jupyter Notebook 界面语言调整

某个版本之后 notebook 界面交互语言会跟系统走，要锁定英文的话：

    - 打开 ~anaconda\Lib\site-packages\notebook\notebookapp.py

    - 找到 `nbui = gettext.translation` 所在行，在参数中加上 languages="eng"

---

## Jupyter Notebook Autoreload

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

## Win32com 各种报错

`AttributeError: module 'win32com.gen_py.xxxxxxx' has no attribute 'CLSIDToClassMap'`：

运行

        import win32com
        print(win32com.__gen_path__)

如果用 jupyter notebook 运行的话先重启 kernal，再打开代码输出的路径，删掉所有文件，重新运行


