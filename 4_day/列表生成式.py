'''
    列表生成式
'''
import sys

def main():
    f = [x for x in range(1, 10)]
    print(sys.getsizeof(f))
    print(f)
    f = (x for x in range(1, 10))
    print(sys.getsizeof(f))
    print(f)
    for var in f:
        print(var)
if __name__ == "__main__":
    main()