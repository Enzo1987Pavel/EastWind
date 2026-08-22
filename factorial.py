input_string = input("Введите целое число: ")


def factorial_interact(n: int):
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    result = 1
    for i in range(2, n + 1):  # начинаем с 2, так как умножение на 1 не меняет результат
        result *= i
    print("Ответ: " + str(result) + "\nНажми \"ENTER\" для выхода...")
    return result


factorial_interact(int(input_string))

