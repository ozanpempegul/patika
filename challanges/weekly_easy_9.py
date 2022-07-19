scanned_numbers = []
def HappyNumbers(n):
    if n == 1:
        return True

    sum = 0
    for i in str(n):
        sum += int(i)*int(i)
    print(sum)
    if sum in scanned_numbers:
        return False

    scanned_numbers.append(sum)

    return HappyNumbers(sum)

print(HappyNumbers(8))
