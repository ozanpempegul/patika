pengonal_number_sum = 1
def pentagonal_number(num):
    global pengonal_number_sum
    if num == 1:
        return pengonal_number_sum
    pengonal_number_sum += (num - 1) * 5
    next_num = num - 1
    return pentagonal_number(next_num)



def a(num):
    sum = 1
    for i in range(num):
        sum += i * 5
    return sum

print(a(1))
print(a(3))
print(a(4))
print(a(5))
