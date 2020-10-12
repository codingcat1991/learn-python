import math


class Point(object):
    def __init__(self, x=0, y=0):
        """
        初始化点
        :param x:横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定点
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量
        :param dx: 横坐标移动距离
        :param dy: 纵坐标移动距离
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        :param other:另一个点
        :return:
        """
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def main():
    point1 = Point(1, 4)
    print(point1)
    point1.move_to(2, 2)
    print(point1)
    point1.move_by(1, 1)
    print(point1)
    point2 = Point(6, 7)
    print(point2)
    print(point1.distance_to(point2))


if __name__ == '__main__':
    main()
