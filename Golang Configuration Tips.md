GO TIPS
========

安装环境
---------

1. 下载 [goX.X.X.windows-amd64.msi](https://golang.org/dl/)，安装

2. 将安装路径 ~\Go\bin 加入到系统环境变量 PATH 中

3. 通过 go run test.go 命令行运行

4. Build System on Sublime text - Go

    (1) Tools - build system - new build system

            {
                "shell_cmd": "go run $file",
                # "cmd": ["go", "run", "$file"],
                "selector": "source.go",
                "file_regex": "^\\s*File \"(...*?)\", line ([0-9]*)"
            }

    (2) save as "Go.sublime-build"
