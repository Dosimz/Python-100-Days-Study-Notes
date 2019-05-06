'''
是回文素数吗?
'''
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