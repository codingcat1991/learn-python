"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
Author: zhouju
Version: 0.1
"""

x = float(input("x = "))
if x > 1:
    f = 3 * x - 5
elif x >= -1:
    f = x + 2
else:
    f = 5 * x + 3
print("f(%.2f) = %.2f" % (x, f))
