def PowersofTwo(num):
    if num == 1:
        return "true"
    if num % 2 == 0:
        num = num // 2
        return PowersofTwo(num)
    return "false"


print(PowersofTwo(16))
print(PowersofTwo(15))
