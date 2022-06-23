# 15/15
import math


def ChessboardTraveling(strParam):
    x = int(strParam[1])
    y = int(strParam[3])
    a = int(strParam[6])
    b = int(strParam[8])

    solutions = 0

    if a > x and b > y:
        diff_a = a - x
        diff_b = b - y
        diff = diff_a + diff_b
        if diff == 2:
            solutions = 2
        else:
            solutions = math.factorial(diff) / (math.factorial(diff_a) * math.factorial(diff_b))

    return int(solutions)


print(ChessboardTraveling("(2 2)(4 3)"))
print(ChessboardTraveling("(1 1)(3 3)"))
