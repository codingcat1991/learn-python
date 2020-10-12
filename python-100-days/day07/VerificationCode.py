"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
Author: zhouju
Version: 0.1
Date: 2019-06-11
"""
import random


def generate_verification_code(length):
    char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rst = ""
    for i in range(length):
        rst += random.choice(char_list)
    return rst


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len:验证码长度（默认4个字符）
    :return:由大小写英文字母和数字构成的随机验证码
    """
    all_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == "__main__":
    print(generate_code())
