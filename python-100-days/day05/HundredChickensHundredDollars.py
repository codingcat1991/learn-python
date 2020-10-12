"""
“百钱百鸡”问题
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""


def hundred_chickens_hundred_dollars_1():
    for x in range(20):
        for y in range(33):
            for z in range(100):
                if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
                    print("%d只公鸡，%d只母鸡，%d只小鸡" % (x, y, z))


def hundred_chickens_hundred_dollars_2():
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print("%d只公鸡，%d只母鸡，%d只小鸡" % (x, y, z))


def hundred_chickens_hundred_dollars_3():
    for k in range(0, 4):
        x = 4 * k
        y = 25 - 7 * k
        z = 75 + 3 * k
        print("%d只公鸡，%d只母鸡，%d只小鸡" % (x, y, z))


print("方法1：")
hundred_chickens_hundred_dollars_1()
print("方法2：")
hundred_chickens_hundred_dollars_2()
print("方法3：")
hundred_chickens_hundred_dollars_3()
