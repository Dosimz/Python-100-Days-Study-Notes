class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self, name):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s 正在愉快的玩耍' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片' % self._name)
        else:
            print('%s只能看熊出没' % self._name)

class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s 的 %s 正在学习 %s' % (self._grade, self._name, course))

class Teacher(Person):
    """教师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s 课任教师 %s 正在讲 %s' % (self._title, self._name, course))

def main():
    stu = Student('余一一', 16, '高一')
    stu.study('Python')
    stu.watch_av()
    t = Teacher('余漪', 21, 'coder')
    t.teach('Python 程序设计')
    t.watch_av()

if __name__ == "__main__":
    main()

