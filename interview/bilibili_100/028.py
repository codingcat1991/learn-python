"""
正则表达式判断一个字符串是否是日期
"""
import re


def is_date(s):
    return re.match(r'^\d{4}-\d{2}-\d{2}', s) is not None


print(is_date('2022-12-23'))
print(is_date('202-12-23'))
print(is_date('2022-2-23'))
print(is_date('2022-12-3'))
