def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Деление на ноль невозможно"

def power(x, y):
    return x ** y

def square_root(x):
    import math
    return math.sqrt(x) if x >= 0 else "Нельзя извлечь корень из отрицательного числа"

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Выйти")

    choice = input("Введите номер операции (1-7): ")

    if choice == '7':
        print("До свидания!")
        break

    if choice in ('1', '2', '3', '4', '5', '6'):
        if choice == '6':
            num = input("Введите число: ")
            if is_number(num):
                num = float(num)
                print(f"Корень из {num} = {square_root(num)}")
            else:
                print("Вы ввели строку. Введите число, чтобы продолжить пользоваться калькулятором.")
        else:
            num1 = input("Введите первое число: ")
            num2 = input("Введите второе число: ")

            if is_number(num1) and is_number(num2):
                num1 = float(num1)
                num2 = float(num2)

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '5':
                    print(f"{num1} ** {num2} = {power(num1, num2)}")
            else:
                print("Вы ввели строку. Введите числа, чтобы продолжить пользоваться калькулятором.")
    else:
        print("Неверный ввод. Пожалуйста, введите номер операции от 1 до 7.")

