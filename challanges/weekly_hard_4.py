# 15/15

def RomanNumeralReduction(strParam):
    values_of_roman_numbers = \
        {"I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000}
    initial_value = 0
    for i in strParam:
        initial_value += values_of_roman_numbers[i]

    result = ""
    M_count = initial_value // 1000
    initial_value -= M_count * 1000
    D_count = initial_value // 500
    initial_value -= D_count * 500
    C_count = initial_value // 100
    initial_value -= C_count * 100
    L_count = initial_value // 50
    initial_value -= L_count * 50
    X_count = initial_value // 10
    initial_value -= X_count * 10
    V_count = initial_value // 5
    initial_value -= V_count * 5
    I_count = initial_value

    result += M_count * "M" + D_count * "D" + C_count * "C" + L_count * "L" + X_count * "X" + V_count * "V" + I_count * "I"

    return result



print(RomanNumeralReduction("XXXVVIIIIIIIIII"))
print(RomanNumeralReduction("DDLL"))