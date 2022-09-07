"""
第012集 读取成绩文件排序数据
输入文件：
三列：学号、姓名、成绩
列之间用逗号分割，比如”101,小张，88"
行之间用\n换行分割
，处理：
读取文件，按成绩倒序排列
输出：
排序后的三列数据
"""


def read_file(path):
    grades = []
    row_name = ('sno', 'sname', 'sgrade')
    with open(path, 'r') as f:
        content = f.read()
        rows = content.split('\n')
        for row in rows:
            row_value = row.split(',')
            row_dict = dict(zip(row_name, row_value))
            grades.append(row_dict)
    return grades


def write_file(sorted_data):
    with open('sorted_grade.txt', 'w') as f:
        for i in sorted_data:
            f.write(f"{i['sno']},{i['sname']},{i['sgrade']}\n")


def sort_grade(grades):
    return sorted(grades, key=lambda x: x["sgrade"])


grades = read_file('./grade')
print(sort_grade(grades))
write_file(sort_grade(grades))
