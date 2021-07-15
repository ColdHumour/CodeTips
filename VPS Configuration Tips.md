VPS CONFIGURATION TIPS
=============================



## **基本Linux操作**

一般选择 Ubuntu 18.04

    > passwd
    
    > apt-get update
    > apt-get upgrade
    > apt install net-tools
    
    > ifconfig

---



## **常用工具**

- [IPCheck](http://ip100.info/check)

- [Putty](https://putty.org/)

---



## V2RAY

### 参考资料

- https://guide.v2fly.org/

- https://toutyrater.github.io

- https://www.codercto.com/a/22204.html

- https://tlanyan.me/v2ray-tutorial/

- https://www.lingbaoboy.com/2019/03/v2raywebsocket-tls-web.html

- https://www.4spaces.org/v2ray-nginx-tls-websocket/

### Server 端

    > bash <(curl -L -s https://install.direct/go.sh)

之后可以

    > cat /etc/v2ray/config.json

查看配置文件，或者

    > nano /etc/v2ray/config.json

有需要可以修改 "port", "Id" 和 "alterId" 字段，之后配置启动

    > systemctl enable v2ray
    > systemctl start v2ray

或者

    > service v2ray start

可以使用

    > service v2ray start|stop|status|reload|restart|force-reload

执行相应指令

### Windows 端

(1) 使用v2rayN

下载并解压 [v2rayN](https://github.com/2dust/v2rayN/releases)

配置

- 服务器 -> 添加[Vmess]服务器 -> 填写 地址/端口/ID/AlterID

- 参数设置 -> PAC模式/直连模式

PAC 模式无需其他配置，直连模式需通过浏览器设置代理，如 FoxyProxy

及时检查更新 v2rayN/v2rayCore/PAC，PAC更新需要在PAC模式下运行

(2) Forward Proxy (v2rayN 目前不支持)

在本地连接必须通过代理的情况下，需要在配置文件中特别设置，并用通常方式执行 v2ray.exe。

浏览器端设置同 v2rayN，设置代理到 127.0.0.1:1080，此时网络流为 PC - vmess - internet proxy - vmess server - target，通过 internet proxy 的数据流为加密过的。

修改 v2ray.exe 同目录下的 config.json 中的 outbounds 和 routing 如下：

          "outbounds": [
            {
              "tag": "proxy",
              "protocol": "vmess",
              "settings": {
                "vnext": [
                  {
                    "address": "XXXX",  # 服务器地址
                    "port": XXXX,  # 服务器端口
                    "users": [
                      {
                        "id": "XXXX",  # id
                        "alterId": 64,
                        "email": "t@t.tt",
                        "security": "auto"
                      }
                    ]
                  }
                ]
              },
              "streamSettings": {
                "network": "tcp"
              },
              "mux": {
                "enabled": false,
                "concurrency": -1
              },
              "proxySettings": {
                "tag": "HTTP"
              }
            },
            {
              "tag": "HTTP",
              "protocol": "http",
              "settings": {
                "servers": [{
                  "address": "XXXX",  # 本地代理地址
                  "port": 8002  # 本地代理端口
                }
              ]}
            },
            {
              "tag": "direct",
              "protocol": "freedom",
              "settings": {},
              "proxySettings": {
                "tag": "HTTP"
              }
            },
            {
              "tag": "block",
              "protocol": "blackhole",
              "settings": {
                "response": {
                  "type": "http"
                }
              }
            }
          ],
          "routing": {
            "domainStrategy": "IPIfNonMatch",
            "rules": [
              {
                "type": "field",
                "outboundTag": "block",
                "domain": [
                  "geosite:category-ads-all"
                ]
              },
              {
                "type": "field",
                "outboundTag": "direct",
                "domain": [
                  "geosite:private",
                  "geosite:tld-cn",
                  "geosite:cn"
                ]
              },
              {
                "type": "field",
                "outboundTag": "proxy",
                "domain": ["geosite:geolocation-!cn"]
              },
              {
                "type": "field",
                "outboundTag": "proxy",
                "network": "tcp,udp"
              }
            ]
          }



### Android 端

下载并安装 [V2rayNG（推荐）](https://github.com/2dust/v2rayNG/releases) 或 [BifrostV](https://apkpure.com/bifrostv/com.github.dawndiy.bifrostv)

手动添加配置，填写 地址/端口/ID/AlterID 即可

推荐仅对部分应用启用 V2ray

---



## SSCLOAK

### 参考资料

- https://github.com/cbeuw/Cloak

- https://github.com/cbeuw/Cloak-android

- https://github.com/HirbodBehnam/Shadowsocks-Cloak-Installer

### Server 端

(1) 安装 git

    > apt-get install git

(2) clone 脚本

    > git clone https://github.com/HirbodBehnam/Shadowsocks-Cloak-Installer.git

(3) 运行脚本

    > bash Shadowsocks-Cloak-Installer/Shadowsocks-Cloak-Installer.sh
    
    > cat /etc/shadowsocks-libev/ckclient.json
    
    > cat /etc/shadowsocks-libev/config.json

如有需要可以自行修改 config.json 中的必要字段，之后配置启动

    > nohup ss-server -c /etc/shadowsocks-libev/config.json &
    
    > jobs -l
    
    > kill -9 ####

### Windows 端

下载并解压 [SSWin](https://github.com/shadowsocks/shadowsocks-windows/releases) 和 [ck-client-windows](https://github.com/cbeuw/Cloak/releases)

配置

- 创建 ckclient.json 并使用与 Server 端相同的配置，核心是 UID 和 PublicKey
  
- 服务器 -> 编辑服务器 -> 填写 地址/端口/密码/加密/插件程序/插件选项
  
- 参数设置 -> PAC模式，需通过浏览器设置代理，如 FoxyProxy

### Android 端

下载并安装 [SSAndroid](https://github.com/shadowsocks/shadowsocks-android/releases) 和 [Cloak-Android](https://github.com/cbeuw/Cloak-android/releases)

手动添加配置，填写 地址/端口/密码/加密/插件配置，插件配置核心是 UID 和 PublicKey

推荐仅对部分应用启用 SSCloak

---

## VPS Server Hosts

- https://www.vultr.com

- https://www.linode.com

- https://bandwagonhost.com

- https://www.cloudsigma.com

- https://www.kamatera.com

- https://www.hostinger.com

- https://www.ionos.com
