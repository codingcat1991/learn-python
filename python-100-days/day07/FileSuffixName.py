"""
设计一个函数返回给定文件名的后缀名
Author: zhouju
Version: 0.1
Date: 2019-06-11
"""


def get_file_suffix_name(file_name):
    """
    返回文件的后缀名
    :param file_name:文件名
    :return:文件名后缀
    """
    start_pos = len(file_name) if file_name.find('.') == -1 else file_name.find('.') + 1
    return file_name[start_pos:]


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename:文件名
    :param has_dot:返回的后缀名是否带点
    :return:文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(get_suffix("sa.w.txt"))
