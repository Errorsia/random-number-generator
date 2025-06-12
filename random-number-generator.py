# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

# Version 2.0

import tkinter as tk
from tkinter import messagebox
from random import *
import ctypes


def check_empty():

    if len(entry1.get()) == 0 or len(entry2.get()) == 0:
        # 输入框为空
        tk.messagebox.showerror(title="Error", message="输入框不能为空!")
        return True
    else:
        return False


def exceed_len_max(num1, num2):

    if len(num1) + len(num2) > 77:
        tk.messagebox.showerror(title="Error", message="输入内容过长!")
        return True
    return False


"""
def is_number(str1, str2):

    first_character_str1 = str1[0]
    first_character_str2 = str2[0]

    list_remain_characters = [str1[1:], str2[1:]]
    digits_in_remain_characters = 0
    list_first_character = [first_character_str1, first_character_str2]
    digits_in_first_character = 0

    is_int = False

    total_length_minus_two = len(str1) + len(str2) - 2

    
    这边其实有一个讨巧的办法：
    try:
        int character_input
    except:
        print(character_input)
    
    for list_tmp in list_remain_characters:
        for character_input in list_tmp:
            for character in "1234567890":
                if character_input== character:
                    # print("j, k: %s, %s" % (j, k))
                    digits_in_remain_characters += 1
                    break

    for character_input in list_first_character:
        for character in "1234567890-":
            if character_input == character:
                digits_in_first_character += 1
                break

    # print(total_length_minus_two)
    if digits_in_remain_characters == total_length_minus_two and digits_in_first_character == 2:
        is_int = True

    if is_int:
        return True
    else:
        # print("Error: Nor int number:")
        tk.messagebox.showerror(title="Error", message="请输入整数!")
        return False
"""


def is_number(str1):

    first_character_str1 = str1[0]

    remain_characters = str1[1:]
    digits_in_remain_characters = 0
    digits_in_first_character = 0

    is_int = False

    total_length_minus_one = len(str1) - 1

    """
    这边其实有一个讨巧的办法：
    try:
        int character_input
    except:
        print(character_input)
    """

    for character_input in remain_characters:
        for character in "1234567890":
            if character_input== character:
                # print("j, k: %s, %s" % (j, k))
                digits_in_remain_characters += 1
                break

    character_input = first_character_str1
    for character in "1234567890-":
        if character_input == character:
            digits_in_first_character += 1
            break

    # print(total_length_minus_two)
    if digits_in_remain_characters == total_length_minus_one and digits_in_first_character == 1:
        is_int = True

    if is_int:
        return True
    else:
        # print("Error: Nor int number:")
        tk.messagebox.showerror(title="Error", message="请输入整数!")
        return False



def random_number():
    if check_empty():
        return

    get1 = entry1.get()
    get2 = entry2.get()

    if exceed_len_max(get1, get2):
        return

    # if not is_number(get1, get2):
    #     return

    if (not is_number(get1)) or (not is_number(get2)):
        return

    num1 = int(get1)
    num2 = int(get2)

    if abs(num1) > 10 ** 32 or abs(num2) > 10 ** 32:
        tk.messagebox.showerror(title="Error", message="输入数字过大!")
        return

    if num1 > num2:
        num1, num2 = num2, num1

    result = randint(num1, num2)

    var.set(f"{result}")


root = tk.Tk()
root.title("随机数发生器")

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
root.geometry(f"1280x720+{(screen_width - 1280) // 2}+{(screen_height - 720) // 2}")
root.resizable(False, False)

var = tk.StringVar()

label100 = tk.Label(root, textvariable=var, font=("Arial", 50), height=3)
label100.grid(row=0, column=0, columnspan=2)

label1 = tk.Label(root, text="请输入开始数字(包含):", font=("Arial", 30), width=20, height=1)
label1.grid(row=1, column=0)

entry1 = tk.Entry(root, font=45, width=100)
entry1.grid(row=1, column=1)

label101_text1 = "使用说明:\n\n将随机在输入的两个数之间(左闭右闭)寻找一个随机数\n\n\n"
label101_text2 = "Attention:\n\n请输入一个整数( -10**32 <= n <= 10**32)."
label101 = tk.Label(root, text=label101_text1 + label101_text2, font=45, width=50, height=10)
label101.grid(row=2, column=0, columnspan=2)

label2 = tk.Label(root, text="请输入结束数字(包含):", font=("Arial", 30), width=20, height=1)
label2.grid(row=3, column=0)

entry2 = tk.Entry(root, font=45, width=100)
entry2.grid(row=3, column=1)

label102 = tk.Label(root, text="祝你好运\tGood Luck", font=45, width=50, height=10)
label102.grid(row=4, column=0, columnspan=2)

button1 = tk.Button(root, text="Start", font=30, width=50, height=2, command=random_number)
button1.grid(row=5, column=0, columnspan=2)

var.set("Please enter the two values")


"""
# button5 = tk.Button(root, text = "©", font=30 width = 1, height= 1, command= clean_Button)
# button5.pack()

label2 = tk.Label(root, width=10, font=20, height=2)
label2.grid(row = 3, column = 0, columnspan = 2)

t = tk.Text(root, height=30)
t.grid(row = 5, column = 0, columnspan = 2)
"""

root.mainloop()