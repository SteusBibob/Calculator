print("Привет, я калькулятор, просьба использовать значение до 10 и арифметические выражения '+,-,/,*")
def main(input: str):
    for Examination in "+-*/":
        if Examination in input:
            numbers = input.split(Examination)
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            if num1 > 10:
                return "Числа не должны быть больше 10."
            if num2 > 10:
                return "Числа не должны быть больше 10."
            result = eval(input)
            return result
        return "Используйте только +, -, * или /."
while True:
    numbers = input("Введите значение (или 'выход' для завершения): ")
    print(main(numbers))
