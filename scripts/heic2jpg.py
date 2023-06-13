# -*- coding: utf-8 -*-

"""
heic2jpg.py

将文件夹内的 .heic 文件转换为 .jpg

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2021.03.09
"""

import os
import subprocess

def heic2jpg(folder):
    # PowerShell 脚本见 https://github.com/DavidAnson/ConvertTo-Jpeg
    # 如无法运行 PowerShell 脚本，出现“系统禁止运行脚本”，请以管理员身份运行 PowerShell，执行
    # PS > set-ExecutionPolicy RemoteSigned

    assert os.path.exists(folder)

    for file in os.listdir(folder):
        if file.split(".")[-1] == "HEIC":
            path = os.path.join(folder, file)
            p = subprocess.Popen([
                "powershell.exe", 
                ".\\heic2jpg.ps1",
                "\"{}\"".format(path)
            ])
            p.communicate()
            os.remove(path)

    for file in os.listdir(folder):
        file1 = file
        for kw in [".HEIC", " - 副本"]:
            file1 = file1.replace(kw, "")

        if file != file1:
            path0 = os.path.join(folder, file)
            path1 = os.path.join(folder, file1)
            if os.path.exists(path1):
                os.remove(path0)
            else:
                os.rename(path0, path1)

if __name__ == "__main__":
    folder = "<Please Specify Folder Path>"
    heic2jpg(folder)
