#!/bin/bash

red='\e[91m'
green='\e[92m'
yellow='\e[93m'
magenta='\e[95m'
cyan='\e[96m'
none='\e[0m'

transport=(
    TCP
    TCP_HTTP
    WebSocket
    "WebSocket + TLS"
    HTTP/2
    mKCP
    mKCP_utp
    mKCP_srtp
    mKCP_wechat-video
    mKCP_dtls
    mKCP_wireguard
    QUIC
    QUIC_utp
    QUIC_srtp
    QUIC_wechat-video
    QUIC_dtls
    QUIC_wireguard
    TCP_dynamicPort
    TCP_HTTP_dynamicPort
    WebSocket_dynamicPort
    mKCP_dynamicPort
    mKCP_utp_dynamicPort
    mKCP_srtp_dynamicPort
    mKCP_wechat-video_dynamicPort
    mKCP_dtls_dynamicPort
    mKCP_wireguard_dynamicPort
    QUIC_dynamicPort
    QUIC_utp_dynamicPort
    QUIC_srtp_dynamicPort
    QUIC_wechat-video_dynamicPort
    QUIC_dtls_dynamicPort
    QUIC_wireguard_dynamicPort
    VLESS_WebSocket_TLS
)

ciphers=(
    aes-128-gcm
    aes-256-gcm
    chacha20-ietf-poly1305
)

_sys_timezone() {
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    timedatectl set-timezone Asia/Shanghai
    timedatectl set-ntp true
    echo -e "已将主机设置为 ${yellow}Asia/Shanghai${none} 时区并通过 systemd-timesyncd 自动同步时间。"
}

_sys_time() {
    echo -e "\n主机时间：${yellow}"
    timedatectl status | sed -n '1p;4p'
    echo -e "${none}"
}

_get_ip() {
    IP=$(curl -s https://ipinfo.io/ip)
    [[ -z $IP ]] && IP=$(curl -s https://api.ip.sb/ip)
    [[ -z $IP ]] && IP=$(curl -s https://api.ipify.org)
    [[ -z $IP ]] && IP=$(curl -s https://ip.seeip.org)
    [[ -z $IP ]] && IP=$(curl -s https://ifconfig.co/ip)
    [[ -z $IP ]] && IP=$(curl -s https://api.myip.com | grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}")
    [[ -z $IP ]] && IP=$(curl -s icanhazip.com)
    [[ -z $IP ]] && IP=$(curl -s myip.ipip.net | grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}")
    [[ -z $IP ]] && echo -e "\n$red 换个机器吧！$none\n" && exit
}

curl() {
  $(type -P curl) -L -q --retry 5 --retry-delay 10 --retry-max-time 60 "$@"
}

check_if_running_as_root() {
  if [[ "$UID" -ne '0' ]]; then
    echo "WARNING: The user currently executing this script is not root. You may encounter the insufficient privilege error."
    read -r -p "Are you sure you want to continue? [y/n] " cont_without_been_root
    if [[ x"${cont_without_been_root:0:1}" = x'y' ]]; then
      echo "Continuing the installation with current user..."
    else
      echo "Not running with root, exiting..."
      exit 1
    fi
  fi
}

identify_the_operating_system_and_architecture() {
  if [[ "$(uname)" == 'Linux' ]]; then
    case "$(uname -m)" in
      'i386' | 'i686')
        MACHINE='32'
        ;;
      'amd64' | 'x86_64')
        MACHINE='64'
        ;;
      'armv5tel')
        MACHINE='arm32-v5'
        ;;
      'armv6l')
        MACHINE='arm32-v6'
        grep Features /proc/cpuinfo | grep -qw 'vfp' || MACHINE='arm32-v5'
        ;;
      'armv7' | 'armv7l')
        MACHINE='arm32-v7a'
        grep Features /proc/cpuinfo | grep -qw 'vfp' || MACHINE='arm32-v5'
        ;;
      'armv8' | 'aarch64')
        MACHINE='arm64-v8a'
        ;;
      'mips')
        MACHINE='mips32'
        ;;
      'mipsle')
        MACHINE='mips32le'
        ;;
      'mips64')
        MACHINE='mips64'
        ;;
      'mips64le')
        MACHINE='mips64le'
        ;;
      'ppc64')
        MACHINE='ppc64'
        ;;
      'ppc64le')
        MACHINE='ppc64le'
        ;;
      'riscv64')
        MACHINE='riscv64'
        ;;
      's390x')
        MACHINE='s390x'
        ;;
      *)
        echo -e "${red}error: The architecture is not supported.${none}"
        exit 1
        ;;
    esac
  else
    echo -e "${red}error: This operating system is not supported.${none}"
    exit 1
  fi
}

identify_command() {
    # system check, yum / apt-get
    if [[ $(command -v apt-get) || $(command -v yum) ]] && [[ $(command -v systemctl) ]]; then
        if [[ $(command -v yum) ]]; then
            CMD="yum"
        else
            CMD="apt-get"
        fi
    else
        echo -e "
        ${red}系统不支持${none}，仅支持 ${red}Ubuntu 16+ / Debian 8+ / CentOS 7+${none} 系统
        " && exit 1
    fi
}

set_environment() {
    $CMD update -y
    if [[ $CMD == "apt-get" ]]; then
        $CMD install -y lrzsz git zip unzip curl wget qrencode libcap2-bin dbus
        ufw disable  # 关闭防火墙
    else
        $CMD install -y lrzsz git zip unzip curl wget qrencode libcap
        systemctl stop firewalld    # 关闭防火墙
        systemctl disable firewalld.service    # 关闭防火墙
    fi
}

# -------------------- enviroment setting --------------------

check_if_running_as_root
identify_the_operating_system_and_architecture
identify_command
_get_ip
set_environment
