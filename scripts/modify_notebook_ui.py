# -*- coding: utf-8 -*-

"""
modify_notebook_ui.py

锁定 jupyter notebook ui 语言为英文

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2020.10.20
"""

import os
import sys

def modify_notebook_ui(languages="en"):
    anaconda_path = [p for p in sys.path if p.endswith("Anaconda3")][0]
    notebookapp = os.path.join(anaconda_path, r"Lib\site-packages\notebook\notebookapp.py")

    assert os.path.exists(notebookapp)

    with open(notebookapp, 'r') as file:
        data = file.readlines()
        
    for i, line in enumerate(data):
        if line.strip().startswith('nbui = gettext.translation'):
            if languages not in line:
                data[i] = line.replace("fallback=True", "languages=\"{}\", fallback=True".format(languages))
            break

    with open(notebookapp, 'w') as file:
        file.writelines(data)

    print("Change UI language to [{}] in {} successfully!".format(languages, notebookapp))


if __name__ == "__main__":
    modify_notebook_ui()
