WOLFRAM ENGINE TIPS
=====================

#### 0. 下载并安装

- https://www.wolfram.com/engine/

如果下载不了的话用

- winget install WolframEngine

安装包会下载到

- %TEMP%\WinGet

解压、安装

#### 1. 激活

- https://account.wolfram.com/

注册 Wolframe ID，邮件确认

打开 wolframescript.exe，按照提示激活

如果不行，打开 wolframe.exe

- https://www.wolframcloud.com/users/user-current/activationkeys

复制一个 Activation Key 到 wolframe 的提示项里

- https://account.wolfram.com/password-generator

根据 MathID 和 Activation Key 生成 Password

输入 wolframe，即可激活

所有信息会保存到 `%USERPROFILE%\AppData\Roaming\WolframEngine\Licensing\mathpass`

#### 2. 安装对应 Jupyter Notebook Kernel

- https://github.com/WolframResearch/WolframLanguageForJupyter/releases

下载 paclet 文件

在该文件位置用命令行打开 `wolframscript`，运行

    PacletInstall["WolframLanguageForJupyter-0.9.3.paclet"]

    Needs["WolframLanguageForJupyter`"]

    ConfigureJupyter["Add"]

完成，现在 jupyter 可以新建 Wolfram Engine 内核的 notebook

#### 3. PythonAPI

- https://reference.wolfram.com/language/WolframClientForPython/

打开 Anaconda Powershell Prompt，定位到本地的 `~\Wolfram Engine\14.2\SystemFiles\Components\WolframClientForPython`，运行

    pip install .

最好结束之后再运行一次

    conda update --all

运行 `ipython`，测试如下代码

    from wolframclient.evaluation import WolframLanguageSession

    from wolframclient.language import wl, wlexpr

    session = WolframLanguageSession()

    session.evaluate(wl.MinMax([1, -3, 0, 9, 5]))

    session.terminate()

如果报错 "WolframKernelException: Cannot locate a kernel automatically. Please provide an explicit kernel path."

加入参数

    session = WolframLanguageSession(r"<full path>\Wolfram Engine\14.2\WolframKernel.exe")

或者修改 `~\Anaconda3\Lib\site-packages\wolframclient\utils\environment.py` 中的 `def _installation_directories()`，在搜索路径中加入

    "<full path>\Wolfram Engine"

这样在 `ipython` 中直接运行

    session = WolframLanguageSession()

    session.evaluate(wl.MinMax([1, -3, 0, 9, 5]))

    session.terminate()

就不会报错了
