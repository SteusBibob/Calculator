def main(input: str):
    for Examination in "+-*/":  # Examination это переменная :)
        if Examination in input:
            parts = input.split(Examination)
            num1, num2 = validate_numbers(parts)
            return calculate (num1, num2, Examination)

def validate_numbers(parts: list[str]):
    if not parts[0]:
        raise ValueError("Нет аргумента")
    if not parts[1]:
        raise ValueError("Нет аргумента")
    if '.' in parts[0] or '.' in parts[1]:
        raise ValueError('Используй только целые числа')
    try:
        num1 = int(parts[0])
        num2 = int(parts[1])
    except ValueError:
        return
    if num1 > 10 or num2 > 10:
        raise ValueError('Числа не могут быть больше 10')
    if num1 < 0 or num2 < 0:
        raise ValueError('Числа отрицательные')
    return num1, num2

def calculate(num1, num2, parts):
    if parts == "+":
        return int(num1) + int(num2)
    elif parts == "-":
        return int(num1) - int(num2)
    elif parts == "*":
        return int(num1) * int(num2)
    elif parts == "/":
        return int(num1) / int(num2)
while True:
    operation_1 = input("Введите значение: ")
    print(main(operation_1))



