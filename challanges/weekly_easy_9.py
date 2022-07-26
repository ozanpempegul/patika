scanned_numbers = []
def HappyNumbers(n):
    if n == 1:
        return True

    sum = 0
    for i in str(n):
        sum += int(i)*int(i)
    if sum in scanned_numbers:
        return False

    scanned_numbers.append(sum)

    return HappyNumbers(sum)

for i in range(10):
    print(HappyNumbers(i), i)
