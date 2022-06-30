# 10/10

from itertools import permutations

def PermutationStep(num):
    str_num = str(num)
    numbers = []
    for i in str_num:
        numbers.append(i)


    number_and_diff = [num, num]
    comb = permutations(numbers, len(numbers))
    for i in comb:
        temp = i
        temp_str = ""
        for j in temp:
            temp_str += j
        number = int(temp_str)
        difference = int(temp_str) - num
        if difference > 0 and difference < number_and_diff[1]:
            number_and_diff = [number, difference]

    if number_and_diff[0] == num:
        return -1
    return number_and_diff[0]


print(PermutationStep(321))
print(PermutationStep(123))
print(PermutationStep(11121))
print(PermutationStep(41352))
