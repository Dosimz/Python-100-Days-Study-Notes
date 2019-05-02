"""
@property 装饰器
"""

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # 访问器 - getter 方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter 方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age
    
    def play(self):
        if self._age <= 16:
            print('%s正在玩斗地主.' % self._name)
        else:
            print('%s正在昆特牌.' % self._name)

def main():
    person = Person('余一', 14)
    person.play()
    person.age = 21
    person.name = 'asd'
    person.play()

if __name__ == "__main__":
    main()

