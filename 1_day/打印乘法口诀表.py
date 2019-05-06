"""
打印乘法口诀表

"""
for i in range(1,10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j),  end = '\t')
    print()