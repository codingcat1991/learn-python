"""
在屏幕上显示跑马灯文字
Author: zhouju
Version: 0.1
Date: 2019-06-11
"""
import os
import time


def marquee_text():
    content = "北京欢迎你!"
    while True:
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    marquee_text()
