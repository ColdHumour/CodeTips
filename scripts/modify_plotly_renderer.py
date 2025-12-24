# -*- coding: utf-8 -*-

"""
modify_plotly_renderer.py

解决 plotly 默认 renderer 不在 jupyter notebook 中显示的问题

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2025.12.02
"""

import os
import sys

def modify_plotly_renderer(value="notebook"):
    anaconda_path = [p for p in sys.path if p.endswith("Anaconda3")][0]
    matplotlib_rcsetup = os.path.join(anaconda_path, r"Lib\site-packages\plotly\io\_renderers.py")

    assert os.path.exists(matplotlib_rcsetup)

    with open(matplotlib_rcsetup, 'r') as file:
        data = file.readlines()
        
    for i, line in enumerate(data):
        if line.startswith('renderers.default = '):
            data[i] = line.replace("default_renderer", "\"{}\"".format(value))
            break

    with open(matplotlib_rcsetup, 'w') as file:
        file.writelines(data)

    print("change plotly default renderer to [{}] succesfully!".format(value))


if __name__ == "__main__":
    modify_plotly_renderer()
