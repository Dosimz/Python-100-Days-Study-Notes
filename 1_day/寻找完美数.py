"""
寻找完美数
判断规则: 一个恰好等于它自身的真因子(除了自身以外的所有约数)之和
        > 约数: 余为零

Date: 2019-4-25 10:40
"""
from functools import reduce
def add(x, y):
    return x + y

lists = []
n = int(input('请输入一个数来判断...(例如:6;28;496;8128;33550336)'))
for factor in range(1, n-1):
    if n % factor == 0:
        lists.append(factor)
if reduce(add, lists) == n:
    print("完美数!" + str(n))
else:
    print('正常数  -_-`')