LINUX AND BASH
=============================

- `passwd`: 修改密码
- `apt-get update -y`: 更新软件列表，默认全选 yes
- `apt-get upgrade -y`: 更新软件，默认全选 yes

- `[Ctrl + u]`: 清空当前输入
- `clear`: 清屏
- `echo -e <info>`: 转义后输出

        # 可使用 echo -e "${<colorname>}<info>$none" 输出彩色字符
        red='\e[91m'
        green='\e[92m'
        yellow='\e[93m'
        magenta='\e[95m'
        cyan='\e[96m'
        none='\e[0m'

- `ls -l`: 列出当前文件目录
- `cd`
- `rm -f <file>`: 删除 file
- `rm -rf <folder>`: 删除 folder
- `chmod +x <file>`: 可执行

- `cat /proc/sys/kernel/random/uuid`: 生成随机 uuid
- `shuf -i<start>-<end> -n1`: 生成一个在 start 到 end 之间的随机数（两端包含）

- `curl -sS -o <file> <url>`: 输出 url 内容至 file
- `git clone <url> <folder>`: clone repo 至指定位置

- 文件条件

        [[ -e FILE ]]       # 存在
        [[ -d FILE ]]       # 目录
        [[ -f FILE ]]       # 文件
