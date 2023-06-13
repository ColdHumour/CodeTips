# -*- coding: utf-8 -*-

"""
modify_wind_login_info.py

解决 wind 每次登录的字符串显示

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2020.02.25
"""

import os


def modify_wind_login_info():
    info = os.popen(r'reg query "HKEY_CURRENT_USER\Software\Wind Information Co., Ltd\Wind金融终端"').read()
    windpath = [line.split("  ")[-1] for line in info.split("\n")
                if line.strip().startswith("Path")][0]
    windpy = os.path.join(windpath, "x64", "WindPy.py")
    assert os.path.exists(windpy)

    with open(windpy, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        if "ix=x.find('site-packages')" in line:
            data[i] = data[i].replace("site-packages", "lib\\site-packages")
            data[i+1] = data[i+1].replace("site-packages", "lib\\site-packages")
            break

    for i, line in enumerate(data):
        if 'print("Welcome' in line:
            if not line.strip().startswith("#"):
                for j in range(i, i+4):
                    data[j] = data[j].replace("print", "# print")
                data[i+4] = data[i+4].replace("\n", "pass\n")
            break

    with open(windpy, 'w') as file:
        file.writelines(data)

    print("Wind login info is modified successfully!")

if __name__ == "__main__":
    modify_wind_login_info()
