"""
输入一个正整数判断它是不是素数

Date: 2019-04-25 12:30
"""

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))  # 平方跟函数 sqrt
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
if is_prime and num != 1:
    print('%d 是素数' % num)
else:
    print('%d 不是素数' % num)