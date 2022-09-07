"""
合并多个文本文件
"""


def read_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return content


def write_file(content, path):
    with open(path, 'w') as f:
        f.write(content)


def merge_files(files: list, new_file):
    content = ""
    for file in files:
        content += read_file(file)
    write_file(content, new_file)


merge_files(['grade.csv', 'teacher.csv', 'grade'], 'merged_file')
