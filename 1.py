def main(input: str):
    for Examination in "+-*/": #Examination это переменная :)
        if Examination in input:
            parts = input.split(Examination)
            num1 = parts[0]
            num2 = parts[1]

            try:
                num1 = int(num1)
                num2 = int(num2)

                validation = validate_numbers(num1, num2)
                if validation:
                    return validation

                return calculate(num1, num2, Examination)

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

def validate_numbers(num1, num2):
    if num1 > 10 or num2 > 10:
        return 'Числа не могут быть больше 10'
    if num1 < 0 or num2 < 0:
        return 'Числа отрицательные'
    return None

def calculate(num1, num2, Examination):
    if Examination == "+":
        return num1 + num2
    elif Examination == "-":
        return num1 - num2
    elif Examination == "*":
        return num1 * num2
    elif Examination == "/":
        return num1 / num2

while True:
    operation_1 = input("Введите значение: ")
    print(main(operation_1))
