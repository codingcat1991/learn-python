"""
验证密码是否符合规范
写一个函数，验证密码是否满足条件
1.长度位于[6,20]之间
2. 必须包含至少1个小写字母
3. 必须包含至少1个大写字母
4. 必须包含至少1个数字
5. 必须包含至少1个特殊字符
返回
True, None
或者 False，原因
"""
import re


def is_valid(s):
    if not 6 <= len(s) <= 20:
        return False, "长度位于[6,20]之间"
    if not re.findall('[a-z]+', s):
        return False, "必须包含至少1个小写字母"
    if not re.findall('[A-Z]+', s):
        return False, "必须包含至少1个大写字母"
    if not re.findall('[0-9]+', s):
        return False, "必须包含至少1个数字"
    if not re.findall('[^0-9a-zA-Z]+', s):
        return False, "必须包含至少1个特殊字符"
    return True


print(is_valid('1qA#'))
print(is_valid('1A#11111'))
print(is_valid('1q#11111'))
print(is_valid('A#dcasdcas'))
print(is_valid('1qA11111'))
print(is_valid('1qA#11111'))
