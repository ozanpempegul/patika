# 5/10
symbols = "+="


def SimpleSymbols(strParam):
    reverse_input = strParam[::-1]
    for i in range(len(strParam)):
        if strParam[i] not in symbols:
            if strParam.find("+") > i or reverse_input.find("+") > len(strParam) - i:
                return False
    return True


print(SimpleSymbols("f++d+"))
print(SimpleSymbols("+d+=3=+s+"))
print(SimpleSymbols("++d+===+c++==a"))
print(SimpleSymbols("+d===+a+"))  # failed case
print(SimpleSymbols("aaaa"))  # failed case

