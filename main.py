import math

try:
    a = int(input("Введите первое число: "))
    dei = input("Введите действие (+, -, *, /): ")
    b = int(input("Введите второе число: "))
except ValueError:
    print("Ошибка: Введены некорректные данные. Пожалуйста, введите числа.")
    exit()
finally:
    print("Ввод завершен.")

# Проверка корректности действия
if dei not in ["+", "-", "*", "/"]:
    print("Ошибка: Неправильное действие. Используйте +, -, *, /.")
    exit()

# Выполнение операции
match dei:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        if b == 0:
            print("Ошибка: На ноль делить нельзя.")
            exit()
        result = a / b

print(f"Результат: {result}")