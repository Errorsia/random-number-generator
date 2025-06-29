# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

import os
from random import randint


# EASTER_EGG = 1
# Times = 0

def trick_input():
    """
    用于加载作弊输入

    :returns: A list if there is a valid trick input, None otherwise
    """

    # 判断作弊文件是否存在
    if not os.path.isfile('./EnableSpecialInput.txt'):
        return

    # 检测文件作弊大小. 防止文件过大, 加载时间过长
    if os.path.getsize('./EnableSpecialInput.txt') > 5000:
        return

    # 加载文件
    with open('./EnableSpecialInput.txt', 'r') as trick_file:
        # 读取文件, 去除换行符
        first_line = trick_file.readline().rstrip()
        # 增加大小写支持(大小写不敏感)
        second_line = trick_file.readline().strip().replace('r', 'R')

    # 检查是否为目标文件格式
    if first_line != '=====EnableSpecialInput=====':
        return

    return handle_trick_input(second_line)


def handle_trick_input(line):
    """
    用于处理作弊输入

    :returns: A list if there is a valid trick input, None otherwise
    """

    if not line:
        return None

    trick_input_str_list = divide_string(line)
    if any(tmp != 'R' and not is_integer(tmp) for tmp in trick_input_str_list):
        return None

    return trick_input_str_list


def is_integer(string):
    """
    判断是否为整数
    判断字符串内容是否为整数

    # 附: 之前写的代码有些复杂, 已经被放弃

    # 之前使用的是遍历每一个字符, 判断是否合法

    # 现在换了一个思路, 十分简洁

    :param string: 输入字符串
    :returns: True if string is an integer, False otherwise
    """

    try:
        int(string)
        return True
    except ValueError:
        return False


def is_empty_string(string):
    """
    判断字符串是否为空字符串

    :param string: Any string
    :return: True if string isn't empty string, False otherwise
    """

    return not bool(string)


def exceed_len_max(str1, str2, str3):
    """
    检查字符串是否超出长度限制

    :param str1: 输入框一
    :param str2: 输入框二
    :param str3: 输入框三(排除的数)
    :return: True if input is too long, False otherwise
    """

    return len(str1) + len(str2) > 77 or len(str3) > 100


def out_of_range(integer):
    """
    检查整数是否超出范围限制

    :param integer: Any str
    :return: True if input is out of range, False otherwise
    """

    return abs(integer) > 10 ** 32


def divide_string(input_string):
    cleaned = input_string.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
    cleaned = cleaned.replace(';', ',').replace('；', ',').replace('，', ',')
    return [s for s in cleaned.split(',') if s]


def handle_exception_input(exception_string):
    """
    处理输入异常x
    处理需要排除的数√

    :param exception_string: 输入字符串
    :returns: True if input is valid, False otherwise
    """

    if not exception_string:
        return True, []

    items = divide_string(exception_string)
    if any(not is_integer(i) for i in items):
        return False, []

    return True, [int(x) for x in items]


def generate_random_int(num1, num2, list_except_number):
    """
    生成一个num1~num2(做闭右闭, 从小到大排列)的随机整数, 保证生成的随机数不在list_except_number中。

    :param num1: 随机数的下界（包含）。
    :param num2: 随机数的上界（包含）。
    :param list_except_number: 一个列表，其中包含了a~b之间的所有整数。
    :returns: 一个num1~num2的随机整数，不在list_except_number中。
    :raises ValueError: 如果list_except_number中包含了所有num1~num2之间的整数。
    """

    if not num2 - num1 >= 10 ** 5:
        if set(range(num1, num2 + 1)).issubset(set(list_except_number)):
            raise ValueError("list_except_number太全，无法生成")

    result = randint(num1, num2)
    while result in list_except_number:
        result = randint(num1, num2)
    return result
