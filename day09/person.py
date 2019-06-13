class Person(object):
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
        if self.age <= 16:
            print('%s在玩飞行棋.' % self._name)
        else:
            print('%s在玩斗地主.' % self._name)


def main():
    p1 = Person('jack', 12)
    p1.play()
    p1.age = 19
    p1.play()

    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    person._is_gay = True


if __name__ == '__main__':
    main()
