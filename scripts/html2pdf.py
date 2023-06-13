# -*- coding: utf-8 -*-

"""
html2pdf.py

将 html 转换为 pdf

@author: Wu Yudi
@email: jasper.wuyd@gmail.com
@date: 2020.07.22
"""

import os
import subprocess
import sys
import time
import win32api
import win32con
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def html2pdf():
    FIREFOX = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    target_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    os.chdir(target_folder)

    br = webdriver.Firefox(firefox_binary=FirefoxBinary(FIREFOX))

    # 载入网页
    br.get(sys.argv[1])
    time.sleep(20)
    title = br.title

    # 按下 ctrl + s
    win32api.keybd_event(0x11, 0, 0, 0)
    win32api.keybd_event(0x53, 0, 0, 0)
    win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(3)

    # 按下 Enter
    win32api.keybd_event(0x0D, 0, 0, 0)
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(3)

    br.close()

    # 定位文件
    file_path = os.path.join(target_folder, "{}_files".format(title))
    html_path = os.path.join(target_folder, "{}.html".format(title))
    if not os.path.exists(html_path):
        html_path = os.path.join(target_folder, "{}.htm".format(title))
    if not os.path.exists(html_path):
        raise FileNotFoundError

    # 转换
    pdf_path = os.path.join(target_folder, "{}.pdf".format(title))
    os.system("wkhtmltopdf --allow \"{}\" \"{}\" \"{}\"".format(file_path, html_path, pdf_path))

    time.sleep(3)

    os.system("explorer \"{}\"".format(target_folder))

if __name__ == "__main__":
    html2pdf()
