OPEN WEBUI CONFIG TIPS
==========================

### A. WINDOWS本地

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

#### 3. 配置 MCP



---------------

### B. LINUX云服务器

#### 0. 安装 docker

    curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
    
    sudo systemctl enable --now docker

#### 1. 拉取镜像并运行

    sudo docker run -d -p 127.0.0.1:3000:8080 \
      --add-host=host.docker.internal:host-gateway \
      -v open-webui:/app/backend/data \
      --name open-webui \
      --restart always \
      ghcr.io/open-webui/open-webui:main

    sudo docker ps

    sudo docker logs open-webui

#### 2. 本地访问

    ssh -L {本地port}:127.0.0.1:3000 {usr}@{server ip}

    # 如不知道 ip 可用 `curl ifconfig.me` 查

如果服务器不能直接访问，但是可以通过 socks5 访问，语句改成

    ssh -o ProxyCommand="\"~\Git\mingw64\bin\connect.exe\" -S 127.0.0.1:{socks5 port} %%h %%p" -L {本地port}:127.0.0.1:3000 {usr}@{server ip}

然后浏览器打开 `http://localhost:{本地port}` 即可

#### 3. 控制

    sudo docker stop/start/restart open-webui

#### 4. 升级

先备份数据以防万一

    # 备份当前数据卷到当前目录
    sudo docker run --rm \
      -v open-webui:/source \
      -v $(pwd):/backup \
      alpine \
      tar czf /backup/openwebui-backup-$(date +%Y%m%d).tar.gz -C /source .

然后重新拉取容器

    # 1. 停止并删除当前容器（卷不会被删除）
    sudo docker rm -f open-webui

    # 2. 拉取最新镜像
    sudo docker pull ghcr.io/open-webui/open-webui:main

    # 3. 用完全相同的参数重建容器（注意保留了卷）
    sudo docker run -d \
      -p 127.0.0.1:3000:8080 \
      --add-host=host.docker.internal:host-gateway \
      -v open-webui:/app/backend/data \
      --name open-webui \
      --restart always \
      ghcr.io/open-webui/open-webui:main

如果不想每次重新登录，可以先生成密钥

    openssl rand -hex 32

然后以后每次带密钥运行

    sudo docker run -d \
      -p 127.0.0.1:3000:8080 \
      --add-host=host.docker.internal:host-gateway \
      -v open-webui:/app/backend/data \
      -e WEBUI_SECRET_KEY="你刚才复制的密钥" \
      --name open-webui \
      --restart always \
      ghcr.io/open-webui/open-webui:main

