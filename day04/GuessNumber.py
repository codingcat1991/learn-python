"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Author: zhouju
Version: 0.1
"""

from random import randint

number = randint(0, 100)
count = 0
while True:
    count += 1
    guess = int(input("请输入："))
    if number > guess:
        print("猜小了！")
    elif number < guess:
        print("猜大了！")
    else:
        print("猜对了！")
        break
print("你总共猜了%d次" % count)
if count > 7:
    print("你的智商明显不足！")
