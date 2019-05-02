"""
在屏幕上显示(滚动)跑马灯文字

Date: 2019-4-28 11:24
"""
# import os
# import time

# def main():
#     content = '在屏幕上显示跑马灯文字......'
#     while True:
#         os.system('clear')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]

# if __name__ == "__main__":
#     main()

"""
设计一个指定长度的验证码(由大小写字母和数字构成)
"""

# import random

# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码

#     :param code_len: 验证码的长度(默认4个字符)

#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, len(all_chars)-1)
#         code += all_chars[index]
#     return code

"""
设定一个函数返回给定文件的后缀名

"""

# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名称

#     :param filename: 文件名
#     :param has_dot: 返回的数据是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos+1
#         return filename[index:]
#     else:
#         return ''

"""
设计一个函数返回列表中最大和第二大的元素

"""

# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m1 = x[index]
#             m2 = m1
#         else:
#             m2 = x[index]
#     return m1, m2

"""
计算指定年月日是这一年的第几天
"""

# def is_leap_year(year):
#     """
#     判  断指定的年份不是闰年

#     :pa ram year: 年份
#     :re turn: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 100 == 0

# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的那一天
#     :param year: 年 
#     :param month: 月
#     :param day: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)]
#     total = 0
#     for index in range(month-1):
#         total += days_of_month[index]
#     return  total + date

# def main():
#     print(which_day(1970, 11, 11))

# if __name__ == "__main__":
#     main()

"""
打印杨辉三角

"""
def main():
    num = int(input('多少行呢?'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()