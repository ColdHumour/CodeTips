#!/bin/bash

[[! -f /etc/codetips/vps/utils.sh]] && return 1

# $MACHINE, $CMD, $IP
. "/etc/codetips/vps/utils.sh"

clear

# ---------------- params and path ----------------
TMP_FILE="$(mktemp)"
ZIP_FILE="/tmp/v2ray.zip"
V2RAY_FOLDER="/usr/bin/v2ray/"

CONFIG_JSON="/etc/v2ray/config.json"
UUID=$(cat /proc/sys/kernel/random/uuid)
PORT=$(shuf -i20001-65535 -n1)

# ---------------- fetch v2ray files ----------------

# echo $TMP_FILE
# curl -sS -H "Accept: application/vnd.github.v3+json" -o "$TMP_FILE" 'https://api.github.com/repos/v2fly/v2ray-core/releases/latest'
# RELEASE_VERSION="$(sed 'y/,/\n/' "$TMP_FILE" | grep 'tag_name' | awk -F '"' '{print $4}')"

RELEASE_VERSION="v4.45.2"  # 5.0 以上好像有bug

echo -e "Latest v2ray version: $yellow$RELEASE_VERSION$none"

DOWNLOAD_LINK="https://github.com/v2fly/v2ray-core/releases/download/$RELEASE_VERSION/v2ray-linux-$MACHINE.zip"
echo -e "Downloading v2Ray archive: $yellow$DOWNLOAD_LINK$none"

curl -sS -H 'Cache-Control: no-cache' -o "$ZIP_FILE" "$DOWNLOAD_LINK"

unzip -o $ZIP_FILE -d $V2RAY_FOLDER
chmod +x "$V2RAY_FOLDER{v2ray,v2ctl}"

# ---------------- config server ----------------

mkdir -p /var/log/v2ray
mkdir -p /etc/v2ray

# service
cat >/lib/systemd/system/v2ray.service <<-EOF
[Unit]
Description=V2Ray Service
Documentation=https://www.v2ray.com/ https://www.v2fly.org/
After=network.target nss-lookup.target
[Service]
# If the version of systemd is 240 or above, then uncommenting Type=exec and commenting out Type=simple
#Type=exec
Type=simple
# This service runs as root. You may consider to run it as another user for security concerns.
# By uncommenting User=nobody and commenting out User=root, the service will run as user nobody.
# More discussion at https://github.com/v2ray/v2ray-core/issues/1011
User=root
Environment="V2RAY_VMESS_AEAD_FORCED=false"
#CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
#AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
NoNewPrivileges=true
ExecStart=/usr/bin/env v2ray.vmess.aead.forced=false /usr/bin/v2ray/v2ray run -config /etc/v2ray/config.json
#Restart=on-failure
Restart=always
[Install]
WantedBy=multi-user.target
EOF

# copy config file
cp -f "/etc/codetips/vps/kcp.json" $CONFIG_JSON

# change port, uuid
sed -i "9s/<port>/$PORT/; 14s/<uuid>/$UUID/" $CONFIG_JSON

# ban ad
ban_ad="/etc/codetips/vps/ad.json"
sed -i "/\/\/include_ban_ad/r $ban_ad" $CONFIG_JSON
sed -i "s#//include_ban_ad#,#" $CONFIG_JSON

# ---------------- run service ----------------
systemctl enable v2ray
systemctl start v2ray

echo
echo -e "$yellow 地址 (Address) = $cyan$IP$none"
echo
echo -e "$yellow 端口 (Port) = $cyan$PORT$none"
echo
echo -e "$yellow 用户ID (User ID / UUID) = $cyan$UUID$none"
echo
echo -e "$yellow 额外ID (Alter Id) = ${cyan}0${none}"
echo
echo -e "$yellow 传输协议 (Network) = ${cyan}kcp$none"
echo
echo -e "$yellow 伪装类型 (header type) = ${cyan}dtls$none"
echo
