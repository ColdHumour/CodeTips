CYTHON TIPS
=============================

---

参考资料：

http://cython.org/

Cython: A Guide to Python Programmers

---

编译器选择
------------------

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


编译及使用
-------------------

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

- ipython note book 直接使用Cython代码

    运行：

        %load_ext Cython

    而后直接使用magic syntax

        %%cython
        cdef ...

    运行即可在其他cell调用编译好的函数
         
注意事项
----------------

- 数据类型
    
    运算过程中需要考虑溢出问题与变量转换问题