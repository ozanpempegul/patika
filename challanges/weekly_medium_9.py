def TripleDouble(num1, num2):
    numbers_of_num1 = set(str(num1))
    counter = 0
    for i in numbers_of_num1:
        if f"{i}{i}{i}" in str(num1) and f"{i}{i}" in str(num2):
            counter += 1
    return counter


print(TripleDouble(451999277, 41177722899))
