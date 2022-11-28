VPS CONFIGURATION TIPS
=============================



## **基本Linux操作**

一般选择 Ubuntu 21.10 x64

    > passwd
    
    > apt-get update
    > apt-get upgrade
    > apt install net-tools
    > apt install firewalld
    
    > ifconfig

---



## **常用工具**

- [IPCheck1](http://ip100.info/check)

- [IPCheck2](https://www.toolsdaquan.com/ipcheck/)

- [Putty](https://putty.org/)

---



## V2RAY

1. 准备工作

### 参考资料

- https://guide.v2fly.org/

- https://toutyrater.github.io

- https://tlanyan.me/v2ray-tutorial/

- https://www.4spaces.org/install-v2ray-on-debian-2021/

- https://www.itblogcn.com/article/1501.html

### VPS Server Hosts

- [Vultr](https://www.vultr.com): cloud instance; no ipv6

- https://www.linode.com

- https://bwh88.net/

- https://www.cloudsigma.com

- https://www.kamatera.com

- https://www.hostinger.com

- https://www.ionos.com

2. 快速部署

参考 https://www.itblogcn.com/article/1501.html

### Server 端

    > bash <(curl -s -L https://raw.githubusercontent.com/xyz690/v2ray/master/go.sh)

### 检查状态

    > systemctl status v2ray

如果 failed 首先检查运行命令是否 `/usr/bin/v2ray/v2ray run -config /etc/v2ray/config.json`，为否则

    > nano /usr/lib/systemd/system/v2ray.service

修改 `ExecStart=` 后面的对应部分，然后

    > systemctl daemon-reload; systemctl restart v2ray

再检查是否 failed，如果仍是，则用

    > /usr/bin/v2ray/v2ray run -config /etc/v2ray/config.json

查看报错信息，并修改配置文件

    > nano /etc/v2ray/config.json

再 restart 看直到 active 为止

3. 手动完整部署

### Server 端

    > bash <(curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh)
    > bash <(curl -L https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-dat-release.sh)

修改配置文件

    > nano /usr/local/etc/v2ray/config.json

主要修改 "port", "id"，其中 uuid 可以[在线生成](https://www.uuidgenerator.net/)，示例文本为

          {
            "inbounds": [{
                "port": <port>,
                "protocol": "vmess",
                "settings": {
                  "clients": [{
                      "id": "<uuid>",
                      "alterId": 0
                  }]
                }
            }],
            "outbounds": [{
                "protocol": "freedom",
                "settings": {}
            }]
          }

修改好可以查看配置文件

    > cat /usr/local/etc/v2ray/config.json

然后需要检查端口是否开通 tcp

    > sudo ufw status verbose
    > sudo ufw allow <port>/
    > sudo ufw allow <port>/tcp
    > systemctl enable firewalld.service
    > systemctl start firewalld.service
    > firewall-cmd --zone=public --list-ports
    > firewall-cmd --zone=public --add-port=<port>/tcp --permanent
    > firewall-cmd --zone=public --add-port=<port>/udp --permanent

之后配置启动

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
