"""
设计一个指定长度的验证码(由大小写字母和数字构成)
"""

import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    code = ''
    for _ in range(code_len):
        index = random.randint(0, len(all_chars)-1)
        code += all_chars[index]
    return code