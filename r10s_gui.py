import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root, logic_module):
        self.logic = logic_module
        self.root = root
        self.var = tk.StringVar()
        self.entry1 = self.entry2 = self.entry3 = None
        self.label_var = None
        self.trick_list = self.logic.trick_input() or []
        self.EASTER_EGG = 1
        self.Times = 0

        self.setup_ui()

    def setup_ui(self):
        self.root.title("随机数发生器")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"1280x720+{(screen_width - 1280) // 2}+{(screen_height - 720) // 2}")
        self.root.resizable(False, False)

        tk.Label(self.root, textvariable=self.var, font=("Arial", 50), height=3).grid(row=0, column=0, columnspan=12)

        self.add_labeled_entry("请输入开始数字(包含):", 1)
        self.add_labeled_entry("请输入结束数字(包含):", 2)
        self.add_labeled_entry("排除的数字(可留空):", 3)

        tk.Label(self.root, text="祝你好运\tGood Luck", font=("Arial", 20), width=50, height=2).grid(row=5, column=0, columnspan=12)

        tk.Button(self.root, bg="cyan", text="Start", font=30, width=40, height=2, command=self.generate).grid(row=6, column=0, columnspan=4)
        tk.Button(self.root, bg="cyan", text="一键清除", font=30, width=40, height=2, command=self.clean_inputs).grid(row=6, column=4, columnspan=4)
        tk.Button(self.root, bg="cyan", text="使用说明", font=30, width=40, height=2, command=self.instructions).grid(row=6, column=8, columnspan=4)

        self.var.set("Please enter two integers🤓")

    def add_labeled_entry(self, text, row):
        label = tk.Label(self.root, text=text, font=("Arial", 30), width=26)
        label.grid(row=row, column=0, columnspan=6)

        entry = tk.Entry(self.root, font=45, width=80)
        entry.grid(row=row, column=6, columnspan=6)

        if row == 1:
            self.entry1 = entry
        elif row == 2:
            self.entry2 = entry
        elif row == 3:
            self.entry3 = entry

    @staticmethod
    def instructions():
        msg = "\n使用说明:\n\n程序将在输入范围内生成随机数（左闭右闭）\n生成的随机数不会出现在排除列表中。\n\n请输入整数（-10^32 到 10^32）"
        messagebox.showinfo(title="Instructions", message=msg)

    def clean_inputs(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.var.set("Please enter two integers🤓")

        if self.EASTER_EGG % 99 == 0:
            messagebox.showinfo("Bonus", "被你发现了ヾ(≧▽≦*)o!")
        elif self.EASTER_EGG % 5 == 0:
            self.var.set("©2024 Errorsia. All Rights Reserved")

        self.EASTER_EGG += 1

    def generate(self):
        self.Times += 1
        get1 = self.entry1.get()
        get2 = self.entry2.get()
        get3 = self.entry3.get()

        if self.logic.is_empty_string(get1) or self.logic.is_empty_string(get2):
            self.var.set('ERROR')
            messagebox.showerror("Error", "输入框不能为空!")
            return

        if self.logic.exceed_len_max(get1, get2, get3):
            self.var.set('ERROR')
            messagebox.showerror("Error", "输入内容过长!")
            return

        if not (self.logic.is_integer(get1) and self.logic.is_integer(get2)):
            self.var.set('ERROR')
            messagebox.showerror("Error", "请输入整数!")
            return

        num1, num2 = int(get1), int(get2)
        if abs(num1) > 10**32 or abs(num2) > 10**32:
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
            messagebox.showerror("Error", "范围错误，全部被排除了！")
            self.var.set('ERROR')
