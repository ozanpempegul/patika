kaprekars_constant_counter = 0
def kaprekars_constant(num):
    global kaprekars_constant_counter
    if num == 6174:
        return kaprekars_constant_counter
    kaprekars_constant_counter += 1
    num_list = []
    for i in str(num):
        num_list.append(i)
    while len(num_list) < 4:
        num_list.append("0")
    num_list.sort()
    smaller_number = int("".join(num_list))
    num_list.reverse()
    bigger_number = int("".join(num_list))
    result = bigger_number - smaller_number
    return kaprekars_constant(result)


print(kaprekars_constant(2111))

