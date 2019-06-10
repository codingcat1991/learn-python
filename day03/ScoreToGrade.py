"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Author: zhouju
Version: 0.1
"""

score = int(input("请输入成绩："))
if score >= 100 or score < 0:
    print("请输入0-100的成绩！")
    exit()
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print("%d对应的等级为%s" % (score, grade))
