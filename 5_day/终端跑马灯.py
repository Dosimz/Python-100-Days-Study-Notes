"""
在屏幕上显示(滚动)跑马灯文字

Date: 2019-4-28 11:24
"""
import os
import time

def main():
    content = '在屏幕上显示跑马灯文字......'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == "__main__":
    main()