JULIA CONFIGURATION TIPS
=============================

## Julia

参考网页 https://datatofish.com/add-julia-to-jupyter/

1. 下载地址：https://julialang.org/

2. 添加到 Julia 到环境变量： ~\Julia-X.X.X\bin

---

## Jupyter Notebook

1. 设置 Pkg [镜像服务器](https://blog.csdn.net/yijiaobani/article/details/100007879)，如果网速够可以跳过

        > using Pkg
        > Pkg.add("PkgMirrors")

        > using PkgMirrors
        > PkgMirrors.setmirror("ZJU")

如果 PowerShell 版本不够，安装 [Microsoft Windows Management Framework 4.0](https://www.microsoft.com/en-us/download/details.aspx?id=40855)，之后重启电脑。

2. 添加 IJulia

        > Pkg.add("IJulia")

3. 配置 Jupyter Notebook

为了避免和 python 开发环境混淆，建议 julia 程序都放到另一个独立的环境中去，因此配置文件做独立的修改

复制 ~\.jupyter\jupyter_notebook_config.py 为 ~\.jupyter\julia_config.py，同样设置

        c.NotebookApp.notebook_dir = u'F:\\lab_julia\\'     # 工作路径
        c.FileContentsManager.root_dir = u'F:\\julia\\notebooks'    # Notebook存储路径

        # 注：如果Notebook存储路径中有与工作路径下同名的文件夹（大小写不敏感），则会自动切换工作路径

而后在 cmd 默认路径下创建 start_julia_notebook.cmd，内容为

        jupyter notebook --config="~\.jupyter\julia_config.py" --port=3456

4. 启动 Jupyter Notebook

在命令行默认路径下执行 start_julia_notebook.cmd 即可

---

## Juno

参考网页 http://docs.junolab.org/latest/

1. 安装 [Atom](https://atom.io/) 

2. 安装 Juno

    Atom 中打开 Install 面板（Ctrl + ,），搜索 "uber-juno"，安装。

    打开 Packages > Juno > Settings，添加路径 ~\Julia-X.X.X\bin\julia.exe

