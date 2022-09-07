"""
Python实现不同文件关联
grade.csv
语文,101,小张,94
语文,102,小王,64
语文,103,小李,62
语文,104,小赵,55
语文,105,小强,91
数学,101,小张,53
数学,102,小王,82
数学,103,小李,86
数学,104,小赵,93
数学,105,小强,72
英语,101,小张,92
英语,102,小王,80
英语,103,小李,73
英语,104,小赵,93
英语,105,小强,51
teacher.csv
语文,于老师
数学,树老师
英语,影老师
"""

import pandas as pd

grades = pd.read_csv('grade.csv', names=['course', 'class', 'name', 'score'])
teachers = pd.read_csv('teacher.csv', names=['course', 'teacher'])
print(pd.merge(grades, teachers, on='course'))
