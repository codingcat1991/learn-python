"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re


def main():
    username = input('请输入用户名：')
    qq_number = input('请输入QQ号：')
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    m2 = re.match(r'^[1-9]\d{4,11}$', qq_number)
    print(str(m1))
    print(str(m2))
    if not m1:
        print('请输入有效的用户名.')
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息有效')


if __name__ == '__main__':
    main()
