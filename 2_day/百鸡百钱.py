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