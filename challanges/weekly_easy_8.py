# 10/10

def TwoSum(arr):
    i = 1
    result = ""
    while i < len(arr) - 1:
        j = i + 1
        while j < len(arr):
            if arr[j] + arr[i] == arr[0]:
                result += f"{arr[i]},{arr[j]} "
            j += 1
        i += 1
    if result:
        return result
    return -1
