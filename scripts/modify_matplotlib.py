# -*- coding: utf-8 -*-

"""
modify_matplotlib.py

解决 matplotlib 中文显示问题

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2020.02.12
"""

import os
import sys

def modify_matplotlib(font="Microsoft YaHei Mono"):
    anaconda_path = [p for p in sys.path if p.endswith("Anaconda3")][0]
    matplotlib_rcsetup = os.path.join(anaconda_path, r"Lib\site-packages\matplotlib\mpl-data\matplotlibrc")

    assert os.path.exists(matplotlib_rcsetup)

    with open(matplotlib_rcsetup, 'r') as file:
        data = file.readlines()
        
    for i, line in enumerate(data):
        if line.startswith('#font.sans-serif'):
            if font not in line:
                data[i] = line.replace(": ", ": {}, ".format(font))
            break

    with open(matplotlib_rcsetup, 'w') as file:
        file.writelines(data)

    print("Add [{}] into {} successfully!".format(font, matplotlib_rcsetup))


if __name__ == "__main__":
    modify_matplotlib()
