OPEN WEBUI CONFIG TIPS
==========================

#### 0. 下载并安装

- https://pypi.org/project/open-webui/

打开 anaconda prompt，定位到文件位置

    pip install open-webui~.tar.gz

期间可能要手动卸载一些库，再重新安装，挺折磨人的

安装完成后

    conda update --all
    conda clean -a
    pip cache purge

#### 1. 运行与配置

在命令行中运行

    open-webui serve

首次登录设置用户名、邮箱、密码，如果自动生成了 `.webui_secret_key` 文件，手动打开并增加长度到32位以上，可以省一个 WARNING

配置API：`左下头像 - 管理员面板 - 外部连接 - 管理 OpenAI 接口连接 - 右侧+号`

如果需要 jupyter 作为 code interpreter，新起一个 jupyter notebook，写好相应的配置文件，然后改设置

#### 2. DEBUG

- OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.

    改环境变量，增加 KMP_DUPLICATE_LIB_OK，值为 TRUE

    ！注意环境变量修改生效后需要关闭 console 重新运行，下同

- HUGGING FACE 太卡了

    改环境变量，增加 HF_ENDPOINT，值为 https://hf-mirror.com

- WARNING: USER_AGENT

    改环境变量，增加 USER_AGENT，值可以写成 OpenWebUI/1.0 (Windows; Local; Dev)

- WARNING: CORS_ALLOW_ORIGIN

    改环境变量，增加 CORS_ALLOW_ORIGIN，值为 http://localhost:8080

- ERROR: DNS

    - 如果能正常访问
        
        打开 ~Anaconda3\Lib\site-packages\aiohttp\resolver.py，把 `import aiodns` 改成 `import aiodns1`

    - 如果能通过代理正常访问

        写个 bat 脚本，先修改环境变量，再运行程序即可，这样的问题仅仅在于用不同API时需要重启服务

            set ALL_PROXY=socks5://127.0.0.1:12345
            set HTTPS_PROXY=socks5://127.0.0.1:12345
            set HTTP_PROXY=socks5://127.0.0.1:12345
            set NO_PROXY=localhost,127.0.0.1,0.0.0.0,::1

            open-webui serve
