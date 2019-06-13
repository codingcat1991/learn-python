import math


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print('周长%.2f' % t.perimeter())
        print('面积%.2f' % t.area())
    else:
        print('不能构成三角形')


if __name__ == '__main__':
    main()
