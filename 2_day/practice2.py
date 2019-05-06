
"""
百鸡百钱
判断规则: 公鸡五钱,母鸡三钱,三小鸡一钱.百钱买百鸡.
a: 公鸡, b: 母鸡, c: 小鸡

Version: 0.1
Author: 余漪

Date： 2019-4-26 10：29 am
"""

for a in range(20):
    for b in range(33):
        if (100-a-b)/3 + 5*a + 3*b == 100:
            print('百钱百鸡!')
            print('公鸡', a)
            print('母鸡', b)
            print('小鸡', 100-a-b) 


"""
### 题目: 
> 5个人(ABCDE)夜间合伙捕鱼,然后睡去,清晨依次醒来分鱼
> A - 把鱼分成5份扔掉多的一条拿走自己的那份
> B - 把鱼分成5份扔掉多的一条拿走自己的那份
> C - 把鱼分成5份扔掉多的一条拿走自己的那份
> D - 把鱼分成5份扔掉多的一条拿走自己的那份
> E - 把鱼分成5份扔掉多的一条拿走自己的那份
> 五人至少捕到多少条鱼？

Date： 2019-4-26 10：46 am
"""

fish = 1
while True:
    total = fish
    is_enouge = True
    for _ in range(5):
        if total % 5 == 1:
            total = (total-1) // 5 * 4
        else:
            is_enouge = False
            break
            print('这鱼不对')
    if is_enouge:
        print('这鱼%d条' % fish)
        break
    fish += 1

"""
斐波那契数列
像这样： 1,1,2,3,5,8,13,21,34,...

Date: 2019-04-26 3:07 pm
"""

def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b
    # print("")
fib(2)

"""
回文素数

"""
def is_prime(numSpaces):
    prime = True
    for j in range(2,numSpaces-1):
        if numSpaces % j == 0:
            prime = False
    if numSpaces < 11:
        prime = False        
    return prime
# print(is_prime(2))
num = 1
while True:
    numSpace = num
    if str(numSpace)[::-1] == str(numSpace) and is_prime(numSpace):
        print('这是回文', numSpace)
    num += 1