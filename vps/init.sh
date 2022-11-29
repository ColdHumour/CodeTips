#!/usr/bin/env bash

pushd /etc
git clone https://github.com/ColdHumour/CodeTips /etc/codetips
popd

chmod +x /etc/codetips/vps/{mincfg.sh,utils.sh}

sed -i "s/\r//" /etc/codetips/vps/mincfg.sh
sed -i "s/\r//" /etc/codetips/vps/utils.sh

