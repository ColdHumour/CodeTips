GO TIPS
========

安装环境
---------

1. 下载 [goX.X.X.windows-amd64.msi](https://golang.org/dl/)，安装

2. 将安装路径 ~\Go\bin 加入到系统环境变量 PATH 中

3. 通过 go run test.go 命令行运行

4. sublime text 3 插件

    - golang build

    - golang tools

    - 安装完后进入 Preferences | Package Settings | Golang Config | Settings - User，添加

            {
                "PATH": "~/go/bin",
                "GOPATH": "~/go"
            }

    - 之后 Ctrl + B 即可编译运行
