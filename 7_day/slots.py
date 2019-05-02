"""
** __slots__ 魔法
用来限定自定义类型的对象只能绑定某些属性,通过定义 __slots__ 变量来进行限定.对子类不生效.
"""

class Person(object):

    # 限定 Person 对象只能绑定 _name,_age 和 _gender 属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩斗地主' % self.name)
        else: 
            print('%s正在玩昆特牌' % self.name)

def main():
    person = Person('余一', 21)
    person.play()
    person.age = 14
    person.play()
    person._gender = '男'
    # 'Person' object has no attribute '_is_good'
    # person._is_good = True      

if __name__ == "__main__":
    main()

