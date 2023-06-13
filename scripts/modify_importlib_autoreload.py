# -*- coding: utf-8 -*-

"""
modify_importlib_reload.py

解决 jupyter notebook 中 autoreload 警告问题

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2020.02.12
"""

import os
import sys

def modify_importlib_reload():
    anaconda_path = [p for p in sys.path if p.endswith("Anaconda3")][0]
    reload_path = os.path.join(anaconda_path, "Lib\\importlib\\__init__.py")

    with open(reload_path, 'r') as file:
        data = file.readlines()
        
    for i, line in enumerate(data):
        if 'ModuleNotFoundError' in line:
            data[i-1] = "        if spec:\n"
            data[i]   = "            _bootstrap._exec(spec, module)\n"
            data[i+1] = ""
            break

    with open(reload_path, 'w') as file:
        file.writelines(data)

    print("importlib.reload() is modified successfully!")


if __name__ == "__main__":
    modify_importlib_reload()
