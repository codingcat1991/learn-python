from abc import abstractmethod, ABCMeta


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print('%s：汪汪汪。。。' % self._nickname)


class Cat(Pet):
    def make_voice(self):
        print('%s：瞄。瞄。瞄。。。' % self._nickname)


def main():
    dog = Dog('小白')
    cat = Cat('小辉')
    dog.make_voice()
    cat.make_voice()


if __name__ == '__main__':
    main()
