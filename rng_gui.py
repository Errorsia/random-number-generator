# -*- coding: utf-8 -*-
# Author: Ariskanyaa <Ariskanyaa@outlook.com>
# Author: Errorsia <Errorsia@outlook.com>
# License: GPL v3

import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root, logic_module):
        """
        初始化变量
        拉起初始化窗口函数

        :param root: 根窗口
        :param logic_module: 逻辑模块
        """
        self.logic = logic_module
        self.root = root
        self.var = tk.StringVar()
        self.entry1 = self.entry2 = self.entry3 = None
        # self.label_var = None

        # 若 trick_input() 返回 None，则赋予空列表作为默认值，确保 trick_list 始终为列表类型
        self.trick_list = self.logic.trick_input() or []

        # Show Easter Egg
        # Condition: (Normally it's on. If Easter_Egg < 1, it's Off)
        self.EASTER_EGG = 1

        # The number of times the random number is generated
        self.Times = 0

        self.setup_ui()

    def setup_ui(self):
        """
        初始化图形化界面

        :return: None
        """
        self.root.title("随机数发生器")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"1280x720+{(screen_width - 1280) // 2}+{(screen_height - 720) // 2}")
        self.root.resizable(False, False)

        tk.Label(self.root, textvariable=self.var, font=("Arial", 50), height=3).grid(row=0, column=0, columnspan=12)

        self.add_labeled_entry("请输入开始数字(包含):", 1)
        self.add_labeled_entry("请输入结束数字(包含):", 2)
        self.add_labeled_entry("排除的数字(可留空):", 3)

        tk.Label(self.root, text="祝你好运\tGood Luck", font=("Arial", 20), width=50, height=2).grid(row=5, column=0,
                                                                                                     columnspan=12)

        tk.Label(self.root, font=45, width=100, height=13).grid(row=4, column=0, columnspan=12)

        tk.Button(self.root, bg="cyan", text="Start", font=30, width=40, height=2, command=self.generate).grid(
            row=6, column=0, columnspan=4)
        tk.Button(self.root, bg="cyan", text="一键清除", font=30, width=40, height=2, command=self.clean_inputs).grid(
            row=6, column=4, columnspan=4)
        tk.Button(self.root, bg="cyan", text="使用说明", font=30, width=40, height=2, command=self.instructions).grid(
            row=6, column=8, columnspan=4)

        self.var.set("Please enter two integers🤓")

    def add_labeled_entry(self, text, row):
        """
        向窗口中添加label

        :param text: 自定义label内容
        :param row: 自定义label所出行(起始为0)
        :return: None
        """
        label = tk.Label(self.root, text=text, font=("Arial", 30), width=26)
        label.grid(row=row, column=0, columnspan=6)

        entry = tk.Entry(self.root, font=45, width=70)
        entry.grid(row=row, column=6, columnspan=6)

        if row == 1:
            self.entry1 = entry
        elif row == 2:
            self.entry2 = entry
        elif row == 3:
            self.entry3 = entry

    @staticmethod
    def instructions():
        msg = (
            "\n使用说明:\n\n本程序将会随机在输入的两个数之间(左闭右闭)寻找一个随机数\n\n"
            "生成的随机数将不会是被排除的数(支持多个数, 用逗号或分号隔开)\n\n\n"
            "Attention:\n\n请输入两个整数( -10^32 <= n <= 10^32)."
        )
        messagebox.showinfo(title="Instructions", message=msg)

    def clean_inputs(self):
        """
        清除输入框
        同时管理彩蛋模块

        :return: None
        """
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.var.set("Please enter two integers🤓")

        # EASTER_EGG module
        if self.EASTER_EGG < 1:
            # EASTER_EGG is off
            pass
        elif self.EASTER_EGG % 99 == 0:
            messagebox.showinfo("Bonus", "被你发现了ヾ(≧▽≦*)o!")
        elif self.EASTER_EGG % 5 == 0:
            self.var.set("©2024 Errorsia. All Rights Reserved")
            # \n算了给你一份文档吧

        self.EASTER_EGG += 1

    def generate(self):
        """
        生成随机数
        由按钮触发

        :return: None
        """
        self.Times += 1

        get1 = self.entry1.get()
        get2 = self.entry2.get()
        get3 = self.entry3.get()

        if self.logic.is_empty_string(get1):
            self.var.set('ERROR')
            messagebox.showerror("Error", "输入框不能为空!")
            return

        if self.logic.is_empty_string(get2):
            self.var.set('ERROR')
            messagebox.showerror("Error", "输入框不能为空!")
            return

        if self.logic.exceed_len_max(get1, get2, get3):
            self.var.set('ERROR')
            messagebox.showerror("Error", "输入内容过长!")
            return

        if not self.logic.is_integer(get1):
            self.var.set('ERROR')
            messagebox.showerror("Error", "请输入整数!")
            return

        if not self.logic.is_integer(get2):
            self.var.set('ERROR')
            messagebox.showerror("Error", "请输入整数!")
            return

        num1, num2 = int(get1), int(get2)
        # 输入整数是否超出范围
        if self.logic.out_of_range(num1) or self.logic.out_of_range(num2):
            self.var.set("ERROR")
            messagebox.showerror("Error", "输入数字过大!")
            return

        if num1 > num2:
            num1, num2 = num2, num1

        valid, except_list = self.logic.handle_exception_input(get3)
        if not valid:
            self.var.set('ERROR')
            messagebox.showerror("Error", "排除数格式错误!")
            return

        if self.trick_list and self.Times <= len(self.trick_list):
            trick_val = self.trick_list[self.Times - 1]
            if trick_val != 'R' and int(trick_val) not in except_list and num1 <= int(trick_val) <= num2:
                self.var.set(str(trick_val))
                return

        try:
            rand_num = self.logic.generate_random_int(num1, num2, except_list)
            self.var.set(str(rand_num))
        except ValueError:
            self.var.set('ERROR')
            messagebox.showerror("Error", "范围错误，全部被排除了！")
