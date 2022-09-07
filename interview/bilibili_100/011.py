"""
第011集 怎样实现学生成绩排序
学生成绩数据格式:
复杂列表,元素是字典或者元组
[
    {'sno': 101, 'sname': "小张", 'sgrade': 88},
    {'sno': 102, 'sname': "小王", 'sgrade': 77},
    {'sno': 103, 'sname': "小李", 'sgrade': 99},
    {'sno': 104, 'sname': "小赵", 'sgrade': 66}
]

"""


def sorted_sgrade(grade_list):
    return sorted(grade_list, key=lambda x: x["sgrade"], reverse=False)


a = [
    {'sno': 101, 'sname': "小张", 'sgrade': 88},
    {'sno': 102, 'sname': "小王", 'sgrade': 77},
    {'sno': 103, 'sname': "小李", 'sgrade': 99},
    {'sno': 104, 'sname': "小赵", 'sgrade': 66}
]
print(sorted_sgrade(a))



for i in a:
    print(f"{i['sno']},{i['sname']},{i['sgrade']}")