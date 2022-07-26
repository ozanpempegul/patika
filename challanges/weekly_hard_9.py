# 15/15

def PatternChaser(strParam):
    result = ["no", ""]  # index0 yes/no, index1 pattern
    for i in range(len(strParam)-2):
        for j in range(i+2, len(strParam)-1):
            if strParam.count(strParam[i:j]) >= 2 and len(strParam[i:j]) > len(result[1]):
                result[0] = "yes"
                result[1] = strParam[i:j]
    if result[1] == "":
        return f"no null"
    return f"{result[0]} {result[1]}"


print(PatternChaser("da2kr32a2"))
print(PatternChaser("abcdefa2klailwq"))
