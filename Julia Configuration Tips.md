JULIA CONFIGURATION TIPS
=============================



## Julia

参考网页 https://datatofish.com/add-julia-to-jupyter/

1. 下载地址：https://julialang.org/

2. 添加到 Julia 到环境变量： ~\Julia-X.X.X\bin

---



## Package Management

从 1.0 开始官方建议使用 `pkg>` 的方式进行包管理，即在 REPL 中输入 `]` 进入包管理模式，`backspace` 或 `ctrl + c` 退出到 `julia>`。

### 准备工作

以下三种配置任选其一：

- 网速够，不做任何操作

- 设置 git 全局代理

- 设置 Pkg [镜像服务器](https://blog.csdn.net/yijiaobani/article/details/100007879)（推荐）

```julia
julia> using Pkg
julia> Pkg.add("PkgMirrors")

julia> using PkgMirrors
julia> PkgMirrors.setmirror("ZJU")
julia> PkgMirrors.setmirror("USTC")
```

注：如果 PowerShell 版本不够，安装 [Microsoft Windows Management Framework 5.1](https://www.microsoft.com/en-us/download/details.aspx?id=54616)，之后重启电脑。

### 当前状态

```julia
julia> Pkg.status()
pkg> status
```

### 安装包

如果是已经配置了镜像服务器，则每次包管理操作时都需要先 `using PkgMirrors`。自动运行的办法是在 `~/<user>/.julia/config/startup.jl` 中加上 `using PkgMirrors`，此后每次运行 REPL 都能看到。

神奇的是，国内镜像服务器也会404，这个时候 `using PkgMirrors` 会遇到 Process Error，需要手动定位到 `<user>\.julia\packages\PkgMirrors\<hash>\cache\current.txt`，改成另一个镜像服务器或者删掉。可以写个脚本来测试，不妨作为最初的练习（见 `./src/startup.jl`）。

另外 Pkg 会自动检测包的依赖及版本环境等，并且会附带安装，代价是慢。同时附带安装的依赖包并不会出现在 status 中，但下次显式安装该包会快很多。

首次使用新包会预编译，很慢，第二次就快了。

```julia
pkg> add IJulia
pkg> add https://github.com/JuliaImages/Images.jl.git
```

从 git repo 安装包时可能遇到 `reference 'refs/heads/master' not found` 错误，此时只能用 Pkg 库安装：

```julia
julia> Pkg.add(PackageSpec(url="https://github.com/BenLauwens/ThinkJulia.jl", rev="master"))
```

### 更新包

```julia
julia> Pkg.update()
pkg> up
```

更新时容易出现的一个问题是 `repository dirty` 错误。暂时不明白问题的机理，一个治标不治本的方法是删掉 `~/<user>/.julia/repositories/general`，重启 REPL，再重新执行 update，这样至少在这一个 session 里问题不会再出现。如此操作会重新下载编译 `general`中的内容，非 常 慢。但好像这个问题不影响 add。

另外每次 update 之后更新的包都需要重新预编译。

所以没事别随便 update。

不定期 update 时，如果出现 `repository dirty` ，删掉 general，再一口气完成全部包管理工作。

### 常用包

- CSV, DataFrames
- Plots, GR, Gadfly
- Flux, ScikitLearn
- PyCall, PyPlot

---



## Jupyter Notebook

### 1. 安装 IJulia

```julia
pkg> add IJulia
```

### 2. 配置 Jupyter Notebook

为了避免和 python 开发环境混淆，建议 julia 程序都放到另一个独立的环境中去，因此配置文件做独立的修改

复制 ~\.jupyter\jupyter_notebook_config.py 为 ~\.jupyter\julia_config.py，同样设置

```python
c.NotebookApp.notebook_dir = u'F:\\lab_julia\\'     # 工作路径
c.FileContentsManager.root_dir = u'F:\\julia\\notebooks'    # Notebook存储路径

# 注：如果Notebook存储路径中有与工作路径下同名的文件夹（大小写不敏感），则会自动切换工作路径
```

而后在 cmd 默认路径下创建 start_julia_notebook.cmd，内容为

```shell
jupyter notebook --config="~\.jupyter\julia_config.py" --port=3456
```

### 3. 启动 Jupyter Notebook

在命令行默认路径下执行 start_julia_notebook.cmd 即可

---



## Juno

参考网页 http://docs.junolab.org/latest/

### 1. 安装 [Atom](https://atom.io/) 

### 2. 安装 Juno

- Atom 中打开 Install 面板（Ctrl + ,），搜索 "uber-juno"，安装。

- 打开 Packages > Juno > Settings，添加路径 ~\Julia-X.X.X\bin\julia.exe
