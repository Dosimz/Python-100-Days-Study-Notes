"""
静态方法
属于类而不属于对象的方法
"""

from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
    a, b, c  = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
        # 也可以通过给类发消息来调用对象方法, 但要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        # print(Triangle.area(t))
    else:
        print('无法构成参数')

if __name__ == "__main__":
    main()
