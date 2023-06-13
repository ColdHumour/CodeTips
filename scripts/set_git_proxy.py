# -*- coding: utf-8 -*-

"""
set_git_proxy.py

用于设置和删除 .gitconfig 中的 proxy 相关

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2020.02.12
"""

import os


def set_git_proxy(url="127.0.0.1:1080"):
    home = os.path.expanduser("~")
    git = os.path.join(home, ".gitconfig")
    with open(git, 'r') as file:
        data = file.readlines()

    flag = False
    for line in data:
        if 'proxy' in line:
            flag = True
            break

    if not flag:
        if data[-1] and not data[-1].endswith("\n"):
            data[-1] += "\n"
        data += [
            "[http]\n",
            "    proxy = http://{}\n".format(url),
            "[https]\n",
            "    proxy = https://{}".format(url),
        ]

    with open(git, 'w') as file:
        file.writelines(data)

    print("Proxy {} is set to {}".format(url, git))


def reset_git_proxy():
    home = os.path.expanduser("~")
    git = os.path.join(home, ".gitconfig")
    with open(git, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        if 'proxy' in line or "[http" in line:
            data[i] = ""

    with open(git, 'w') as file:
        file.writelines(data)

    print("Proxy is removed from {}".format(git))


if __name__ == "__main__":
    # set_git_proxy()
    reset_git_proxy()
