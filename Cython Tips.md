CYTHON TIPS
===============

0. 参考资料

- http://cython.org/

- Cython: A Guide to Python Programmers

---

1. 编译器选择

(1) 64位 Python 3.5 及以上

直接安装[Visual C++ Build Tools 2015](http://go.microsoft.com/fwlink/?LinkId=691126)

(2) 32位 Python 3.3 及以上

详见 [cython wiki](https://github.com/cython/cython/wiki/CythonExtensionsOnWindows)

---

2. 编译及使用

(1) 文件结构

代码保存到 xxx.pyx 文件里，并创建同名 .pxd 文件备用。如果有函数是 cdef 的，则需要在 pxd 文件中声明函数名称才能被其他文件访问到。例如

```python
# in a.pyx
cdef long long c_gcd_int64(long long a, long long b):
    if a == 0 or b == 0:
        return 1
    ...

# in a.pxd
cdef long long c_gcd_int64(long long a, long long b)
```

如此定义后可在同路径其他 pyx 文件中执行

```python
from a cimport c_gcd_int64
```

否则

```python
# in a.pyx
def long long c_gcd_int64(long long a, long long b):
    if a == 0 or b == 0:
        return 1
    ...

# in a.pxd
# nothing here
```

只能

```python
from a import c_gcd_int64
```

对于需要使用 c++ 编译的情况，pyx 和 pxd 头部需要加

```python
# distutils: language = c++
```

(2) 编译

在 pyx 和 pxd 同路径下构建 setup.py，内容示例为

```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

import numpy as np

extensions = []

EXT_FILES = ['c_formula_int64', 'cpp_formula_int64']
for f in EXT_FILES:
    extensions.append(Extension(f, [f + '.pyx']))

EXT_FILES_INC = ['c_linalg_int64', 'c_prime_int64']
for f in EXT_FILES_INC:
    extensions.append(Extension(f, [f + '.pyx'],
                                include_dirs=[np.get_include()]))

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(extensions),
)
```

其中使用 extensions 的目的是为了一次编译多个文件，此外注意到如果用到 numpy 的话需要额外指定 include_dirs

之后命令行运行：

    python setup.py build_ext -i --compiler=msvc

编译完成后同路径下会出现 xxx.c, xxx.h, xxx.cpp 等编译中间文件，最终结果为 xxx.pyd，完成后即可直接 import 或 cimport （视 pxd 配置确定）

(3) jupyter notebook 直接使用Cython代码

运行：

    %load_ext Cython

而后在 cell 开头加上 magic syntax

    %%cython

或者

    %%cython --cplus

接着写 cython 代码并运行，即可在其他 cell 调用编译完成的函数

cell 中可以 cimport 需要的库如 libc, libcpp, 以及自己写的编译好的其他 cython 代码

---

3. 各种 TIPS

(1) 常见数据类型与 numpy 对应

|cython|numpy|
|:-:|:-:|
|short|np.int16|
|long|np.int32|
|long long|np.int64|
|float|np.float32|
|double|np.float64|

使用

```python
ctypedef long long int64
ctypedef vec[int64] ivec
```

定义别名，可以少写很多代码。同时可以看到 ctypedef 支持多层级

cython 默认环境不含 bool，如要使用需要显式导入

```python
from libcpp cimport bool
```

可以大幅降低数据结构的空间占用，在 prime sieve 类型算法中很好用

(2) numpy

需要显式导入两遍

```python
import numpy as np
cimport numpy as np
```

之后对于 np.ndarray 需要特别声明，但是实际声明变量时还需要指定参数

```python
ctypedef np.ndarray arr

arr[long, ndim=1] myarray

cdef arr[long, ndim=2] get_matrix(long N):
    ...
```

(2) 多返回值

在 jupyter notebook 环境中，c++ 类型的代码可以支持 tuple of int 之类的数据结构，但是本地 pyx 和 pxd 编译通过不了

建议使用 vector 等内置容器或者 struct 来传递变量，struct 更优一些，因为还可以作为参数传入

个人偏好写法

```python
cdef struct desc:
    int64 N
    int64 Nrt  # isqrt(N)
    bool flag  # N // Nrt == Nrt
```

但还没掌握比较好的命名法，现在的写法类名、变量名和属性名比较容易混

struct 的声明和实例化可以直接用

```python
cdef desc info

info = desc(4, 2, 0)
```

(3) 函数

cdef 的函数是仅限 cython 环境调用的，例如在 jupyter notebook 中声明的 cdef 函数并不能在其他 cell 里调用。但是 cython 的 def 中可以调用 cdef，只要返回时保证没有无法转换的数据类型就可以。例如可以返回 long, tuple, list, np.ndarray，但不能返回 vector, map, deque 或者 struct 等

对于用作 context 的变量，无论是不对其内容进行修改的（如查表用）或者对其内容进行修改的（如 cache 用），实践中都应该以地址形式传入参数，但调用时无需特别处理。例如

```python
ctypedef vector[long] lvec

cdef long f(long n, lvec cache):
    if n > 5:
        cache[n % 5] = n
        return f(n-5, cache)
    else:
        return cache[n]

def long mask_f():
    cdef:
        long n = 100
        lvec cache = lvec(6, 0)

    return f(n, cache)
```

实际运行效果与 python 中传 dict 或 list 作为引用的情况一样，会实时地修改内存地址中该数据结构的内容。这样效率会高很多。

(4) 数据结构

- libcpp.pair 可以直接仿照 struct 初始化

- map.find(key) == map.end() 表示 map 中不存在 key

- vector 的排序需要额外 from libcpp.algorithm cimport sort，然后执行 sort(vec.begin(), vec.end())

- 容器基本都没有 len, 而是用 .size() 方法获取
