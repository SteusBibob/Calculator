def main(input: str):
    for Examination in "+-*/":  # Examination это переменная :)
        if Examination in input:
            parts = input.split(Examination)
            num1 = parts[0]
            num2 = parts[1]

            return calculate(num1, num2, Examination)

def validate_numbers(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return None
    if num1 > 10 or num2 > 10:
        return 'Числа не могут быть больше 10'
    if num1 < 0 or num2 < 0:
        return 'Числа отрицательные'
    return None

def calculate(num1, num2, Examination):
    try:
        if Examination == "+":
            return int(num1) + int(num2)
        elif Examination == "-":
            return int(num1) - int(num2)
        elif Examination == "*":
            return int(num1) * int(num2)
        elif Examination == "/":
            return int(num1) / int(num2)
    except ValueError:
        if Examination == "+":
            return num1 + num2
        elif Examination == "*":
            try:
                num2 = int(num2)
                return num1 * num2
            except ValueError:
                num1 = int(num1)
                return num1 * num2
        elif Examination == "/":
            return "Делить буквы нельзя"
        elif Examination == "-":
            return "Вычитать буквы нельзя"

while True:
    operation_1 = input("Введите значение: ")
    print(main(operation_1))




