# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

# Version 3.0

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




def is_number(string):

    first_character = string[0]
    remain_characters = string[1:]

    if first_character == "-" and len(string) == 1:
        tk.messagebox.showerror(title="Error", message="请输入整数!")
        return False

    is_int = False

    digits_in_string = 0
    total_length = len(string)

    for character_input in remain_characters:
        for character in "1234567890":
            if character_input== character:
                # print("j, k: %s, %s" % (j, k))
                digits_in_string += 1
                break

    for character in "1234567890-":
        if first_character == character:
            digits_in_string += 1
            break

    if digits_in_string == total_length:
        is_int = True

    if not is_int:
        tk.messagebox.showerror(title="Error", message="请输入整数!")

    return is_int





def generate_random_number():
    if check_empty():
        return

    get1 = entry1.get()
    get2 = entry2.get()

    if exceed_len_max(get1, get2):
        return

    if (not is_number(get1)) or (not is_number(get2)):
        return

    num1 = int(get1)
    num2 = int(get2)

    if abs(num1) > 10 ** 32 or abs(num2) > 10 ** 32:
        tk.messagebox.showerror(title="Error", message="输入数字过大!")
        return

    if num1 > num2:
        num1, num2 = num2, num1



    random_number = randint(num1, num2)


    # legal_exception = None
    exception_input_list = []



    equal_to_exception = False
    equal_number = None
    for tmp_str in exception_input_list:
        if tmp_str == random_number:
            equal_to_exception = True
            equal_number = tmp_str
            break

    if equal_to_exception and equal_number == num1 and num1 == num2:
        print("No output")
        return
    elif equal_to_exception:
        generate_random_number()

    var.set(f"{random_number}")

def clean_input_box():
    entry1.delete("0", tk.END)
    entry2.delete("0", tk.END)
    entry3.delete("0", tk.END)


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


label101_text1 = "\n使用说明:\n\n将随机在输入的两个数之间(左闭右闭)寻找一个随机数\n\n"
label101_text2 = "生成随机数将不会是被排除的数(支持排除多个数, 用逗号或分号隔开)\n\n\n"
label101_text3 = "Attention:\n\n请输入一个整数( -10^32 <= n <= 10^32)."
label101_text = label101_text1 + label101_text2 + label101_text3
label101 = tk.Label(root, text=label101_text, font=45, width=100, height=13)
label101.grid(row=4, column=0, columnspan=2)


label102 = tk.Label(root, text="祝你好运\tGood Luck", font=("Arial", 20), width=50, height=2)
label102.grid(row=5, column=0, columnspan=2)


button1 = tk.Button(root, bg="cyan", text="Start", font=30, width=50, height=2, command=generate_random_number)
button1.grid(row=6, column=0)

button2 = tk.Button(root, bg="cyan", text="一键清除", font=30, width=50, height=2, command=clean_input_box)
button2.grid(row=6, column=1)

var.set("Please enter the two values🤓")


"""
# button5 = tk.Button(root, text = "©", font=30 width = 1, height= 1, command= clean_Button)
# button5.pack()

label2 = tk.Label(root, width=10, font=20, height=2)
label2.grid(row = 3, column = 0, columnspan = 2)

t = tk.Text(root, height=30)
t.grid(row = 5, column = 0, columnspan = 2)
"""

root.mainloop()