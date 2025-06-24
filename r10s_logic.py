import os
from random import randint

# EASTER_EGG = 1
# Times = 0

def trick_input():
    if os.path.isfile('./EnableSpecialInput.txt'):
        with open('./EnableSpecialInput.txt', 'r') as trick_file:
            first_line = trick_file.readline().rstrip()
            second_line = trick_file.readline().strip().replace('r', 'R')

        if first_line != '=====EnableSpecialInput=====':
            return

        return handle_trick_input(second_line)

def handle_trick_input(line):
    if not line:
        return None

    trick_input_str_list = divide_string(line)
    if any(tmp != 'R' and not is_integer(tmp) for tmp in trick_input_str_list):
        return None

    return trick_input_str_list

def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_empty_string(string):
    return not bool(string)

def exceed_len_max(str1, str2, str3):
    return len(str1) + len(str2) > 77 or len(str3) > 100

def divide_string(input_string):
    cleaned = input_string.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')
    cleaned = cleaned.replace(';', ',').replace('；', ',').replace('，', ',')
    return [s for s in cleaned.split(',') if s]

def handle_exception_input(exception_string):
    if not exception_string:
        return True, []

    items = divide_string(exception_string)
    if any(not is_integer(i) for i in items):
        return False, []

    return True, [int(x) for x in items]

def generate_random_int(num1, num2, list_except_number):
    if not num2 - num1 >= 10 ** 5:
        if set(range(num1, num2 + 1)).issubset(set(list_except_number)):
            raise ValueError("list_except_number太全，无法生成")

    result = randint(num1, num2)
    while result in list_except_number:
        result = randint(num1, num2)
    return result
