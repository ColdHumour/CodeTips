# -*- coding: utf-8 -*-

"""
kindleclean.py

清除不必要的书签文件夹

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2020.02.20
"""

import os
import psutil
import shutil
import subprocess


def kindleclean():
    errflag = 1
    for disk in  psutil.disk_partitions():
        volinfo = subprocess.check_output(["cmd", "/c vol {}".format(disk.device.strip("\\"))])
        try:
            volinfo = volinfo.decode("utf-8")
        except UnicodeDecodeError:
            volinfo = volinfo.decode("gbk")
        finally:
            label = volinfo.split("\r\n")[0].split(" ").pop()

        if label.lower() == "kindle":
            errflag = 0
            break

    if errflag:
        raise ValueError("Kindle disk not found!")

    kindlefolder = os.path.join(disk.device, "documents")
    files = os.listdir(kindlefolder)

    ebooks = [f.rsplit(".", maxsplit=1)[0] for f in files if f.split(".").pop() in "txt|pdf|azw3|mobi|kfx"]
    sdrfolders = [f.rsplit(".", maxsplit=1)[0] for f in files if f.endswith("sdr")]
    mismatch = [f for f in sdrfolders if f not in ebooks]
    for f in mismatch:
        shutil.rmtree(os.path.join(kindlefolder, "{}.sdr".format(f)))
        print("{}.sdr is removed from kindle.".format(f))


if __name__ == "__main__":
    kindleclean()
