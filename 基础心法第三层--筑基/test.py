"""时间"""
# from time import time, localtime, sleep

# ctime = localtime(time())
# print(ctime)

"""循环和布尔"""
num = int(input('NUM为:'))
# if num < 6:
#     print('num 小于 6')
# elif num < 9:
#     print('num => (6,9) !')


def alive(num):
    return num > 0

def test(fun):
    print(fun)
    print(type(fun))
    print(fun>0)
test(alive(num))