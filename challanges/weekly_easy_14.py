def LargestPair(num):
    result = 0
    i = 0
    while i < len(str(num)) - 1:
        temp_result = str(num)[i] + str(num)[i+1]
        if int(temp_result) > result:
            result = int(temp_result)
        i += 1

    return result
