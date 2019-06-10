# """
# 从列表中找出最大的或最小的 N 元素
# 堆结构(大根堆/小根堆)
# """

import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]
# print(list2[0]['name'])
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

"""
迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools

a = itertools.permutations('ABCD')
b = itertools.combinations('ABCDE', 3)
c = itertools.product('ABCD', '123')
def fun(x):
    for _ in x:
        print(_)
fun(c)