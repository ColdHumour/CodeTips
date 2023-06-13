# -*- coding: utf-8 -*-

"""
modify_termcolor.py

解决 termcolor 失效问题

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2022.12.1
"""

import os
import sys

def modify_termcolor():
    anaconda_path = [p for p in sys.path if p.endswith("Anaconda3")][0]
    termcolor = os.path.join(anaconda_path, r"Lib\site-packages\termcolor\termcolor.py")

    assert os.path.exists(termcolor)

    with open(termcolor, 'r') as file:
        data = file.readlines()

    for i, line in enumerate(data):
        if "if not _can_do_colour()" in line and "#" not in line:
            data[i] = data[i].replace("if", "# if")
            data[i+1] = data[i+1].replace("return", "# return")
            break

    with open(termcolor, 'w') as file:
        file.writelines(data)

    print("termcolor is modified successfully!")


if __name__ == "__main__":
    modify_termcolor()
