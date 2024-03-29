"""
计算班级的最高分最低分平均分
课程, 班级, 姓名, 分数
语文, 101, 小张, 94
语文, 102, 小王, 64
语文, 103, 小李, 62
语文, 104, 小赵, 55
语文, 105, 小强, 91
数学, 101, 小张, 53
数学, 102, 小王, 82
数学, 103, 小李, 86
数学, 104, 小赵, 93
数学, 105, 小强, 72
英语, 101, 小张, 92
英语, 102, 小王, 80
英语, 103, 小李, 73
英语, 104, 小赵, 93
英语, 105, 小强, 51
"""

import pandas as pd

df = pd.read_csv('class-grade.csv', names=['课程', '班级', '姓名', '分数'])
df = df.groupby(['课程'])
print(df['分数'].max())
print(df['分数'].min())
print(df['分数'].mean())
