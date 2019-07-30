'''
斐波那契数列
像这样： 1,1,2,3,5,8,13,21,34,...
'''
def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b
    # print("")
fib(2)