VPS CONFIGURATION TIPS
=============================


## **常用工具**

- [IPCheck1](http://ip100.info/check)

- [IPCheck2](https://www.toolsdaquan.com/ipcheck/)

- [Putty](https://putty.org/)

---


## **参考资料**

### guide

- https://guide.v2fly.org/

- https://www.4spaces.org/install-v2ray-on-debian-2021/

- https://www.clloz.com/programming/assorted/2019/11/24/v2ray-install-configuration/

- https://ailitonia.com/archives/v2ray%e5%ae%8c%e5%85%a8%e9%85%8d%e7%bd%ae%e6%8c%87%e5%8d%97/

- https://www.itblogcn.com/article/1501.html

### repo

- https://github.com/v2fly/fhs-install-v2ray/

- https://github.com/xyz690/v2ray/tree/master

---


## **VPS Server Hosts**

- [Vultr](https://www.vultr.com): cloud instance; no ipv6

- https://www.linode.com

- https://bwh88.net/

- https://www.cloudsigma.com

- https://www.kamatera.com

- https://www.hostinger.com

- https://www.ionos.com


---

## **Server 端**

在合适的目录下

    > nano init.sh

复制脚本进去，`Ctrl + x`，`y`，`Enter`

    > chmod +x ./init.sh
    > ./init.sh
    > /etc/codetips/vps/mincfg.sh

对照屏幕显示信息设置客户端

可以使用

    > service v2ray start|stop|status|reload|restart|force-reload

执行相应指令

## **Windows 端**

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

## **Android 端**

下载并安装 [V2rayNG（推荐）](https://github.com/2dust/v2rayNG/releases) 或 [BifrostV](https://apkpure.com/bifrostv/com.github.dawndiy.bifrostv)

手动添加配置，填写 地址/端口/ID/AlterID 即可

推荐仅对部分应用启用 V2ray

---
