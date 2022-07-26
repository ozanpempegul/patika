# 10/10
counter = 0
def AdditivePersistence(num):
    global counter
    print(num)
    if num < 10:
        return counter
    counter += 1
    sum = 0
    for i in str(num):
        sum += int(i)
    return AdditivePersistence(sum)


print(AdditivePersistence(99999999999999999999999999999))
