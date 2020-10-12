"""
Craps赌博游戏
Author: zhouju
Version: 0.1
Date: 2019-06-10
"""
from random import randint

money = int(input("请输入游戏筹码："))
while money > 0:
    while True:
        debt = int(input("你目前拥有筹码：%d。请下注：" % money))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    need_to_go_on = False
    if first == 7 or first == 11:
        money = money + debt
        print("玩家掷出了%d点，玩家胜" % first)
    elif first == 2 or first == 3 or first == 12:
        money = money - debt
        print("玩家掷出了%d点，庄家胜" % first)
    else:
        print("玩家掷出了%d点，未分胜负，继续" % first)
        need_to_go_on = True
    while need_to_go_on:
        go_on = randint(1, 6) + randint(1, 6)
        if go_on == first:
            print("玩家掷出了%d点，玩家胜" % go_on)
            money = money + debt
            need_to_go_on = False
        elif go_on == 7:
            print("玩家掷出了%d点，庄家胜" % go_on)
            money = money - debt
            need_to_go_on = False
        else:
            pass
else:
    print("你破产了！")
