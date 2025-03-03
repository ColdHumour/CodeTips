WINDOWS TIPS
=============================


## WINDOWS

#### 当前用户添加管理员权限

`win + r`，运行 gpedit.msc

如不存在 gpedit.msc，新建 .bat 文件如下，保存并右键以管理员身份运行

```
@echo off

pushd "%~dp0"

dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum > List.txt

dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >> List.txt

for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"C:\Windows\servicing\Packages\%%i"

pause
```

运行完成后再重新运行 gpedit.msc

左侧：计算机配置 - 窗口设置 - 安全设置 - 本地策略 - 安全选项

右侧：管理员帐户状态 - 启用


#### 桌面图标空白

任务管理器 - Windows 资源管理器 - 右键 - 重新启动


#### 开关机记录

此电脑 - 管理 - 事件查看器 - windows日志


#### 权限问题

创建 bat 文件

        cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start "" %1"

将 exe 文件拖到 bat 文件上打开


#### 系统文件清理

系统盘（右键）- 属性 - 常规 - 磁盘清理 - 清理系统文件


#### 添加小鹤双拼方案

`win + r`，运行 regedit

在 `\HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS` 下新建字符串值

名为 `UserDefinedDoublePinyinScheme0`，值为 `小鹤双拼*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt`

在输入法设置中设置 小鹤双拼 为默认选择


#### 右键新建没有 txt

`win + r`，运行 regedit

在 `HKEY_CURRENT_USER\Software\Classes\CLSID` 下新建项，重命名为 `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`

在该项下新建项，重命名为 `InprocServer32`

修改 `InprocServer32` 中默认字符串值为空

重启电脑


#### win11 程序卸载后还在 `设置 - 应用 - 安装的应用` 里并且报错

打开 `控制面板 - 程序和功能`，找到对应的条目刷新即可


---


## EXCEL

#### 函数

- 返回元素在序列中的位置，当不需要VLOOKUP时用来查行号或者列号很有用

        =MATCH(A1, B1:B10, 0)

- 根据地址相对位置取值，只要有行列偏移量即可，注意计数从0开始

        =OFFSET(A1, 1, 1)  # 等同于 =B2
        =OFFSET(A1, 0, 0)  # 等同于 =A1

- 根据单元格地址字符串取值，其中地址可以用其他公式生成，然后整体可以嵌套在其他用于计算的函数内

        =INDIRECT("A1")  # 等同于 =A1
        =INDIRECT("Sheet1!A1:B10")

- 字符串转日期，如20170101这种，其他情况可以此类推

        =DATE(LEFT(A1, 4), MID(A1, 5, 2), RIGHT(A1, 2))
        =DATEVALUE(A1)

- 日期转字符串，如2017-01-01，其他情况可以此类推

        =TEXT(A1, "yyyy-mm-dd")

- 字符串双引号

        ="A""B"  # 输出即 A"B

- 第N大的数

        =LARGE(A1:A30, 2)  # 第2大

- 换行符

        CHAR(10)

- 序列公式，即某些函数输入可以是 Range 而非单个的值，按 `Ctrl + Shift + Enter` 执行，执行后公式最外侧会显示 `{}`。此功能配合 SUBTOTAL 等逆天函数可以实现在一个单元格中计算股票一段时间的波动率乃至最大回撤：

        =STDEV.S(A3:A100/A2:A99)*SQRT(245)  # 波动率
        =MIN(A2:A100/SUBTOTAL(4,OFFSET(A2:A100,ROW(A2:A100)-ROW(A2:A100),0,ROW(A2:A100)-ROW(INDIRECT(A2))+1)))-1  # 最大回撤

- 对字符串形式存在的公式求值，需要在 `公式-名称管理器` 中调用 EVALUATE 函数

- `公式-名称管理器` 可以用于定义常量，或者一个需要被反复调用的引用，似乎只需要 eval 一次即可

- `公式-名称管理器` 名称管理器也可以用于定义需要大量反复使用的函数，固定部分参数，相当于 Python 里的 partial

- 批量向前/后补全空值：`F5-定位条件-空值-确定`，键入公式 `= + UP/DOWN`，按 `Ctrl + Enter` 执行


#### 更改默认设置

主要是字体和字号，由于 Excel 新建文件和新建 sheet 的机制不一样，因此需要修改多个地方。

- 文件 - 选项 - 常规 - 新建工作簿时 - 修改字体和字号到想要的样子

- 开始 - 样式 - 单元格样式 - 常规（右键 - 修改） - 修改字体和字号到想要的样子，保存

- `Win + R` 输入 `regedit` 打开注册表编辑器，查看 `HKEY_CLASSES_ROOT\.xlsx\Excel.Sheet.12\ShellNew` 项中的 `FileName` 的值，如果找不到的话可以试试 `C:\Windows\SHELLNEW`

- 打开该文件，`Ctrl + A`，把字体和字号设置成想要的样子，保存

- 如果无法保存，则先复制一份到其他路径下改好，原路径中的文件 `Shift + 右键` 删除，然后把改好的文件重新复制到当前路径下


#### 加密

另存为 - “保存”按钮左边的“工具”下拉选“常规选项”，然后可以分别设置文件打开的密码和修改的密码


