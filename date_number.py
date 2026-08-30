def convert_to_digit(symbol: str) -> int:

    total = sum(int(char) for char in symbol if char.isdigit())

    while total >= 9:
        total = sum(int(digit) for digit in str(total))

    return total


inp_date = input("Print your date of birth: ")
result = convert_to_digit(inp_date)
print(result)
