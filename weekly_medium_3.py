# 10/10

def SwapII(strParam):
    strParam2 = strParam + " "
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    number_counter = 0
    i = 0
    i1 = 0  # will be used for swaping numbers
    i2 = 0  # will be used for swaping numbers
    each_char = []
    while i < len(strParam2):
        if strParam2[i] in letters:
            each_char.append(strParam2[i].swapcase())

        elif strParam2[i] in numbers:
            each_char.append(strParam2[i])
            if number_counter == 0 and strParam2[i + 1] not in numbers:
                i1 = i  # first number's index
                number_counter = 1
            elif number_counter == 0 and strParam2[i + 1] in numbers:
                number_counter = 0
            elif number_counter == 1:
                number_counter += 1

        else:
            each_char.append(strParam2[i])
            number_counter = 0

        if number_counter == 2:
            i2 = i  # second number's index
            number_counter = 0
            each_char.pop(i1)
            each_char.insert(i1, strParam2[i2])
            each_char.pop(i2)
            each_char.insert(i2, strParam2[i1])

        i += 1

    return "".join(each_char)

