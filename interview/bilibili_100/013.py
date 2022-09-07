"""
第013集统计学生成绩高分低分平均分
输入文件：
三列：学号、姓名、成绩
列之间用逗号分割，比如”101,小张，88"
行之间用\n换行分割
输出：最高分、最低分、平均分
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


def max_score(scores):
    return max(scores)


def min_score(scores):
    return min(scores)


def avg_score(scores):
    return sum(scores) / len(scores)


grades = read_file('grade')
scores = [int(i['sgrade']) for i in grades]
print(f"max:{max_score(scores)}")
print(f"max:{min_score(scores)}")
print(f"max:{avg_score(scores)}")
