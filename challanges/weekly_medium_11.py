def off_binary(str_arr):
    decimal_number = int(str_arr[0])
    given_binary = str_arr[1]
    correct_binary = bin(decimal_number)[2:]  # first 2 indexes are "0b"
    off_binary_counter = 0
    i = 0
    while i < len(correct_binary):
        if correct_binary[i] != given_binary[i]:
            off_binary_counter += 1
        i += 1

    return off_binary_counter


print(off_binary(["56", "011000"]))
