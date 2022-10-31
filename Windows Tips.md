COMPUTER CONFIGURATION TIPS
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
