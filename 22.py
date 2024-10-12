def main(input: str):
    for Examination in "+-*/": #Examination это переменная :)
        if Examination in input:
            parts = input.split(Examination)
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
                if Examination == "+":
                    return num1 + num2
                elif Examination == "-":
                    return num1 - num2
                elif Examination == "*":
                    return num1 * num2
                elif Examination == "/":
                    return num1 / num2
            except ValueError:
                if Examination == "+":
                    return num1 + num2
                elif Examination == "*":
                    try:
                        num2 = int(num2)
                        return num1 * num2
                    except ValueError:
                        return num1 * num2
                elif Examination == "/":
                    return "Делить буквы нельзя"
                elif Examination == "-":
                    return "Вычитать буквы нельзя"
    return "Используйте только +, -, *, /"

while True:
    operation_1 = input("Введите значение")
    print(main(operation_1))