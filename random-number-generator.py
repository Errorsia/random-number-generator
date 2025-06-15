# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

# Version 5.0

import tkinter as tk
from tkinter import messagebox
from random import *
import ctypes


# Show Easter Egg
# Current condition (Normally it's on. If Easter_Egg < 1, it's Off):
EASTER_EGG = 1

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
        var.set("©2024 Arthur_xyz. All Rights Reserved")
    elif EASTER_EGG % 11 == 0:
        tk.messagebox.showinfo(title="Bonus", message="被你发现了ヾ(≧▽≦*)o!\n还真有人点了这么多下!")
        # \n算了给你一份文档吧

    EASTER_EGG += 1



def generate():
    """
        生成随机数

        由按钮触发
    """
    get_entry1 = entry1.get()
    get_entry2 = entry2.get()
    get_entry3 = entry3.get()

    if check_empty(get_entry1, get_entry2):
        var.set('ERROR')
        return

    if exceed_len_max(get_entry1, get_entry2, get_entry3):
        var.set('ERROR')
        return

    if not (is_integer(get_entry1) and is_integer(get_entry2)):
        var.set('ERROR')
        return

    num1 = int(get_entry1)
    num2 = int(get_entry2)

    if abs(num1) > 10 ** 32 or abs(num2) > 10 ** 32:
        var.set('ERROR')
        tk.messagebox.showerror(title="Error", message="输入数字过大!")
        return

    if num1 > num2:
        num1, num2 = num2, num1



    exception_input_condition, list_except_number = handle_exception_input(get_entry3)

    if not exception_input_condition:
        var.set('ERROR')

        return

    random_number = generate_random_number(num1, num2, list_except_number)

    var.set(f"{random_number}")

    return



def check_empty(get1,get2):

    if not get1 or not get2:
        # 输入框为空
        tk.messagebox.showerror(title="Error", message="输入框不能为空!")
        return True
    else:
        return False


def exceed_len_max(str1, str2, str3):

    if len(str1) + len(str2) > 77 or len(str3) > 100:
        tk.messagebox.showerror(title="Error", message="输入内容过长!")
        return True
    return False



def is_integer(string):
    """
        判断是否为整数

        # 附: 之前写的代码有些复杂, 已经被放弃
        # 现在换了一个思路, 十分简洁

        Args:
            string: 输入字符串

        Returns:
            True if string is an integer, False otherwise
    """

    try:
        int(string)
        return True
    # 如果转换失败，则书不是整数。
    except ValueError:
        tk.messagebox.showerror(title="Error", message="请输入的整数!")
        return False




def handle_exception_input(exception_string):
    """
        处理输入异常

        Args:
            exception_string: 输入字符串

        Returns:
            True if input is valid, False otherwise
    """

    if not exception_string:
        # Length of exception_string is 0
        # print('Length of exception_string is 0')
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
        分割字符串

        Args:
            input_string: 输入字符串

        Returns:
            列表，包含分割后的字符串
    """

    input_string = input_string.replace(' ', '').replace('\n', '').replace('\r', '')
    string_tmp1 = input_string.replace(';', ',').replace('；', ',').replace('，', ',')


    list_characters = []
    string_tmp2 = ""

    if not string_tmp1[-1] == ",":
        string_tmp1 += ","
    # print(f"string_tmp1: {string_tmp1}")

    for i in string_tmp1:
        if i == ",":
            list_characters.append(string_tmp2)
            string_tmp2 = ""
        else:
            string_tmp2 += i
        # print(f"list_characters:{list_characters}")

    list_characters = [element for element in list_characters if element != '']
    # print(f 'list_characters:{list_characters}')

    return list_characters



def generate_random_number(num1, num2, list_except_number):

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
    """生成一个a~b(做闭右闭, 从小到大排列)的随机整数, 保证生成的随机数不在list1中。

          参数：
                a：随机数的下界（包含）。
                b：随机数的上界（包含）。
                list1：一个从小到大排列的列表，其中包含了a~b之间的所有整数。

          返回：
                一个a~b的随机整数，不在list1中。

          抛出：
                ValueError：如果list1中包含了所有a~b之间的整数。
    """


    if not num2 - num1 >= 10 ** 6:
        # 检查list1是否包含了所有num1~num2之间的整数
        if set(range(num1, num2 + 1)).issubset(set(list_except_number)):
            raise ValueError("list1包含了所有a~b之间的整数，无法生成不在list1中的随机数。")

    # 生成一个随机整数
    random_int = randint(num1, num2)

    # 如果生成的随机数在list_except_number中，则重新生成
    while random_int in list_except_number:
        random_int = randint(num1, num2)

    # 返回生成的随机数
    return random_int




# main window
root = tk.Tk()
root.title("随机数发生器")

# Screen size
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
root.geometry(f"1280x720+{(screen_width - 1280) // 2}+{(screen_height - 720) // 2}")
root.resizable(False, False)

var = tk.StringVar()

label100 = tk.Label(root, textvariable=var, font=("Arial", 50), height=3)
label100.grid(row=0, column=0, columnspan=2)

label1 = tk.Label(root, text="请输入开始数字(包含):", font=("Arial", 30), width=26, height=1)
label1.grid(row=1, column=0)

entry1 = tk.Entry(root, font=45, width=80)
entry1.grid(row=1, column=1)


label2 = tk.Label(root, text="请输入结束数字(包含):", font=("Arial", 30), width=26, height=1)
label2.grid(row=2, column=0)

entry2 = tk.Entry(root, font=45, width=80)
entry2.grid(row=2, column=1)


label3 = tk.Label(root, text="请输入需要排除的数字(可不输入):", font=("Arial", 30), width=26, height=1)
label3.grid(row=3, column=0)

entry3 = tk.Entry(root, font=45, width=80)
entry3.grid(row=3, column=1)


label101_text1 = "\n使用说明:\n\n本程序将会随机在输入的两个数之间(左闭右闭)寻找一个随机数\n\n"
label101_text2 = "生成的随机数将不会是被排除的数(支持多个数, 用逗号或分号隔开)\n\n\n"
label101_text3 = "Attention:\n\n请输入两个整数( -10^32 <= n <= 10^32)."
label101_text = label101_text1 + label101_text2 + label101_text3
label101 = tk.Label(root, text=label101_text, font=45, width=100, height=13)
label101.grid(row=4, column=0, columnspan=2)


label102 = tk.Label(root, text="祝你好运\tGood Luck", font=("Arial", 20), width=50, height=2)
label102.grid(row=5, column=0, columnspan=2)


button1 = tk.Button(root, bg="cyan", text="Start", font=30, width=50, height=2, command=generate)
button1.grid(row=6, column=0)

button2 = tk.Button(root, bg="cyan", text="一键清除", font=30, width=50, height=2, command=clean_input_box)
button2.grid(row=6, column=1)

var.set("Please enter two integers🤓")


root.mainloop()