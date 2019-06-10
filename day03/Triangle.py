"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Author: zhouju
Version: 0.1
"""
import math

a = float(input("请输入边a的长："))
b = float(input("请输入边b的长："))
c = float(input("请输入边c的长："))
if a + b > c and a + c > b and b + c > a:
    print("周长：%.1f" % (a + b + c))
    perimeter = (a + b + c) / 2
    area = math.sqrt(perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c))
    print("面积：%.1f" % area)
else:
    print("不能构成三角形！")
