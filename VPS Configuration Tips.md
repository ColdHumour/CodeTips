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

下载并解压 [v2rayN](https://github.com/2dust/v2rayN/releases)

配置

- 服务器 -> 添加[Vmess]服务器 -> 填写 地址/端口/ID/AlterID

- 参数设置 -> PAC模式/直连模式

PAC 模式无需其他配置，直连模式需通过浏览器设置代理，如 FoxyProxy

及时检查更新 v2rayN/v2rayCore/PAC，PAC更新需要在PAC模式下运行

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
