def main(input: str):
    # Перебираем арифметические операции
    for operation in "+-*/":
        if operation in input:
            # Разделяем строку на две части по символу операции
            parts = input.split(operation)
            num1 = parts[0]
            num2 = parts[1]
            try:
                num1 = int(num1)
                num2 = int(num2)
                if num1 > 10:
                    return 'Числа не могут быть больше 10'
                if num2 > 10:
                    return 'Числа не могут быть больше 10'
                if num1 < 0:
                    return 'Числа отрицательные'
                if num2 < 0:
                    return 'Числа отрицательные'
                if operation == "+":
                    return num1 + num2
                elif operation == "-":
                    return num1 - num2
                elif operation == "*":
                    return num1 * num2
                elif operation == "/":
                    return num1 / num2
            except ValueError:
                if operation == "+":
                    return num1 + num2
                elif operation == "*":
                    try:
                        num2 = int(num2)
                        return num1 * num2
                    except ValueError:
                        return num1 * num2
                elif operation == "/":
                    return "Делить буквы нельзя"
                elif operation == "-":
                    return "Вычитать буквы нельзя"
    return "Используйте только +, -, *, /"

while True:
    operation_1 = input("Введите значение")
    print(main(operation_1))