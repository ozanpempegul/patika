def pentagonal_number(num):
    sum = 1
    return pentagonal_number2(num, sum)



def pentagonal_number2(num, sum):
    if num == 1:
        return sum
    sum += (num - 1) * 5
    next_num = num - 1
    return pentagonal_number2(next_num, sum)

def a(num):
    sum = 1
    for i in range(num):
        sum += i * 5
    return sum

print(pentagonal_number(3))