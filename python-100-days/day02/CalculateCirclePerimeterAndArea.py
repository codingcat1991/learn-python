"""
输入圆的半径计算周长和面积
Author: zhouju
Version: 0.1
"""

import math

radius = float(input('请输入圆的半径：'))
pi = math.pi
perimeter = 2 * pi * radius
area = pi * (radius ** 2)
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
