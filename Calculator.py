import pyfiglet
from os import system, name
import time

class Error(Exception):
    pass

def calculate(a,b,op):
    ops = ["+","-","/","*"]
    if not op in ops:
        raise Error("Недопустимая операция!")
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        if b == 0:
            raise Error("На ноль делить нельзя!")
        else:
            return a + b
    elif op == "*":
        return a * b
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

title = pyfiglet.figlet_format("Calculator",font="larry3d")

while True:
    clear()
    try:
        a = float(input(f"{title}"
        "Добро пожаловать в калькулятор!\n"
        "Допустимые операции: / * + -\n"
        "Введите первое число: "))
    except Error as e:
        print("Должно быть число!")
        time.sleep(3)
    clear()

    try:
        b = float(input(f"{title}"
        "Введите второе число: "))
        clear()
    except Error as e:
        print("Должно быть число!")
        time.sleep(3)

    op = input(f"{title}Введите желаемую операцию: ")
    clear()

    try:
        print(title)
        print(f"\033[32m{calculate(a,b,op)}\033[m")
        time.sleep(5)
    except Error as e:
        print("\033[031mОшибка:",e,"\033[m")
        time.sleep(5)