'''
题目: 
    5个人(ABCDE)夜间合伙捕鱼,然后睡去,清晨依次醒来分鱼
    A - 把鱼分成5份扔掉多的一条拿走自己的那份
    B - 把鱼分成5份扔掉多的一条拿走自己的那份
    C - 把鱼分成5份扔掉多的一条拿走自己的那份
    D - 把鱼分成5份扔掉多的一条拿走自己的那份
    E - 把鱼分成5份扔掉多的一条拿走自己的那份
    五人至少捕到多少条鱼？
'''

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