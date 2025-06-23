# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

# Version 8.1


"""
Update - En:
1. Add and change wrong comments

Update - Zh-cn:
1. 新增和修改了错误注释
"""

import tkinter as tk
from tkinter import messagebox
from random import *
import os

# Show Easter Egg
# Condition: (Normally it's on. If Easter_Egg < 1, it's Off)
EASTER_EGG = 1

Times = 0


def trick_input():
    """
    用于处理作弊输入

    :returns: A list if there is a valid trick input, None otherwise
    """

    if os.path.isfile('./EnableSpecialInput.txt'):

        with open('./EnableSpecialInput.txt', 'r') as trick_file:

            first_line = trick_file.readline()
            second_line = trick_file.readline()

        # 去除换行符
        first_line = first_line.rstrip()
        second_line = second_line.strip()

        # 检查是否为目标文件格式
        if not first_line == '=====EnableSpecialInput=====':
            return

        second_line = second_line.replace('r', 'R')

        # if not second_line:
        #     # Length of exception_string is 0
        #     return None
        return handle_trick_input(second_line)

    else:
        return None


def handle_trick_input(line):
    if not line:
        # Length of exception_string is 0
        return None

    trick_input_str_list = divide_string(line)

    # Is legal trick input
    if any((tmp == 'R' or is_integer(tmp)) == False for tmp in trick_input_str_list):
        return None

    return trick_input_str_list


def instructions():
    instruction = (
        "\n使用说明:\n\n本程序将会随机在输入的两个数之间(左闭右闭)寻找一个随机数\n\n"
        "生成的随机数将不会是被排除的数(支持多个数, 用逗号或分号隔开)\n\n\n"
        "Attention:\n\n请输入两个整数( -10^32 <= n <= 10^32)."
    )
    tk.messagebox.showinfo(title="Instructions", message=instruction)


def clean_input_box():
    """
    清除输入框

    同时管理彩蛋模块
    """
    global EASTER_EGG

    entry1.delete("0", tk.END)
    entry2.delete("0", tk.END)
    entry3.delete("0", tk.END)
    var.set("Please enter two integers🤓")

    # EASTER_EGG module
    if EASTER_EGG < 1:
        pass
    elif EASTER_EGG % 5 == 0:
        var.set("©2024 Errorsia. All Rights Reserved")
    elif EASTER_EGG % 99 == 0:
        tk.messagebox.showinfo(title="Bonus", message="被你发现了ヾ(≧▽≦*)o!\n还真有人点了这么多下!")
        # \n算了给你一份文档吧

    EASTER_EGG += 1


def generate():
    """
    生成随机数
    由按钮触发

    :return: None
    """
    global Times

    Times += 1

    get_entry1 = entry1.get()
    get_entry2 = entry2.get()
    get_entry3 = entry3.get()

    if is_empty_string(get_entry1):
        var.set('ERROR')
        # 输入框为空
        tk.messagebox.showerror(title="Error", message="输入框不能为空!")
        return

    if is_empty_string(get_entry2):
        var.set('ERROR')
        # 输入框为空
        tk.messagebox.showerror(title="Error", message="输入框不能为空!")
        return

    if exceed_len_max(get_entry1, get_entry2, get_entry3):
        var.set('ERROR')
        tk.messagebox.showerror(title="Error", message="输入内容过长!")
        return

    if not is_integer(get_entry1):
        var.set('ERROR')
        tk.messagebox.showerror(title="Error", message="请输入整数!")
        return

    if not is_integer(get_entry2):
        var.set('ERROR')
        tk.messagebox.showerror(title="Error", message="请输入整数!")
        return

    num1 = int(get_entry1)
    num2 = int(get_entry2)

    # Check the range of numbers
    if out_of_range(num1) or out_of_range(num2):
        var.set('ERROR')
        tk.messagebox.showerror(title="Error", message="输入数字过大!")
        return

    if num1 > num2:
        num1, num2 = num2, num1

    exception_input_condition, list_except_number = handle_exception_input(get_entry3)

    if not exception_input_condition:
        var.set('ERROR')
        tk.messagebox.showerror(title="Error", message="请输入整数!")
        return

    if trick_input_list and Times <= len(trick_input_list):

        current_trick_num = trick_input_list[Times - 1]

        if not current_trick_num == 'R':

            if num1 <= int(current_trick_num) <= num2 and not int(current_trick_num) in list_except_number:
                random_number = current_trick_num

                var.set(f"{random_number}")

                return

    random_number = generate_random_number(num1, num2, list_except_number)

    var.set(f"{random_number}")

    return


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
    # 如果转换失败，则书不是整数。
    except ValueError:
        return False


def handle_exception_input(exception_string):
    """
    处理输入异常x
    处理需要排除的数√

    :param exception_string: 输入字符串
    :returns: True if input is valid, False otherwise
    """

    if not exception_string:
        # Length of exception_string is 0
        return True, []

    list_character = divide_string(exception_string)

    if len(list_character) == 0:
        return True, []

    if any(is_integer(element_tmp2) == False for element_tmp2 in list_character):
        return False, []

    # print("\nAll number is int:", end = '')

    int_list_character = []
    for k in list_character:
        int_list_character.append(int(k))
    # int_list_character = [int(k) for k in list_character]

    return True, int_list_character


def divide_string(input_string):
    """
    处理字符
    分割字符串

    :param input_string: 输入字符串
    :returns: 列表，包含分割后的字符串
    """

    input_string = input_string.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
    input_string = input_string.replace(';', ',').replace('；', ',').replace('，', ',')

    list_characters = input_string.split(',')

    list_characters = [element for element in list_characters if element != '']

    return list_characters


def generate_random_number(num1, num2, list_except_number):
    """
    生成一个在num1~num2, 之间的随机数, 且不在list_except_number内

    :param num1: 起始数(较小)
    :param num2: 中止数(较大)
    :param list_except_number: 被排除的数(不会被生成)
    :return:
    """

    try:
        # 调用函数生成随机数
        random_int = generate_random_int(num1, num2, list_except_number)

        # 返回随机数
        return random_int
    except ValueError as error:
        tk.messagebox.showerror(title="Error", message="无法生成, 范围错误, 请检查需要排除的数!")
        print(error)
        return "ERROR"


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
        # 检查list_except_number是否包含了所有num1~num2之间的整数
        if set(range(num1, num2 + 1)).issubset(set(list_except_number)):
            raise ValueError("list_except_number包含了所有num1~num2之间的整数，无法生成不在list_except_number中的随机数")

    # 生成一个随机整数
    random_int = randint(num1, num2)

    # 如果生成的随机数在list_except_number中，则重新生成
    while random_int in list_except_number:
        random_int = randint(num1, num2)

    # 返回生成的随机数
    return random_int


trick_input_list = trick_input()

# main window
root = tk.Tk()
root.title("随机数发生器")

# Screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"1280x720+{(screen_width - 1280) // 2}+{(screen_height - 720) // 2}")
root.resizable(False, False)

var = tk.StringVar()

label100 = tk.Label(root, textvariable=var, font=("Arial", 50), height=3)
label100.grid(row=0, column=0, columnspan=12)

label1 = tk.Label(root, text="请输入开始数字(包含):", font=("Arial", 30), width=26, height=1)
label1.grid(row=1, column=0, columnspan=6)

entry1 = tk.Entry(root, font=45, width=80)
entry1.grid(row=1, column=6, columnspan=6)

label2 = tk.Label(root, text="请输入结束数字(包含):", font=("Arial", 30), width=26, height=1)
label2.grid(row=2, column=0, columnspan=6)

entry2 = tk.Entry(root, font=45, width=80)
entry2.grid(row=2, column=6, columnspan=6)

label3 = tk.Label(root, text="排除的数字(可留空):", font=("Arial", 30), width=26, height=1)
label3.grid(row=3, column=0, columnspan=6)

entry3 = tk.Entry(root, font=45, width=80)
entry3.grid(row=3, column=6, columnspan=6)

label101_text = ''
label101 = tk.Label(root, text=label101_text, font=45, width=100, height=13)
label101.grid(row=4, column=0, columnspan=12)

label102 = tk.Label(root, text="祝你好运\tGood Luck", font=("Arial", 20), width=50, height=2)
label102.grid(row=5, column=0, columnspan=12)

button1 = tk.Button(root, bg="cyan", text="Start", font=30, width=40, height=2, command=generate)
button1.grid(row=6, column=0, columnspan=4)

button2 = tk.Button(root, bg="cyan", text="一键清除", font=30, width=40, height=2, command=clean_input_box)
button2.grid(row=6, column=4, columnspan=4)

button3 = tk.Button(root, bg="cyan", text="使用说明", font=30, width=40, height=2, command=instructions)
button3.grid(row=6, column=8, columnspan=4)

var.set("Please enter two integers🤓")

root.mainloop()
