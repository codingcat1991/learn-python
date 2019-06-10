"""
华氏度转摄氏度
Author: zhouju
Version: 0.1
"""

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8

print('%.1f华氏度=%.1f摄氏度' % (f, c))
