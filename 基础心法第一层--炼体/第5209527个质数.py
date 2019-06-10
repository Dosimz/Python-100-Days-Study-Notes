from math import sqrt

def is_prime(num):
    end = int(sqrt(num))  # 平方跟函数 sqrt
    is_prime = True
    for i in range(2, end + 1):
        if num % i == 0:
            is_prime = False
    return is_prime

x, index = 3, 1
while True:
    if is_prime(x):
        index += 1
        print(index)
    x += 2
    # print(x)
    if index == 5209527:
        print(x)
        break


# print(is_prime(4))