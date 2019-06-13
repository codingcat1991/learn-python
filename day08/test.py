class Test(object):
    def __init__(self, foo):
        self._foo = foo

    def _bar(self):
        print(self._foo)
        print('_bar')


def main():
    t = Test('hello')
    t._bar()
    print(t._foo)


if __name__ == '__main__':
    main()
