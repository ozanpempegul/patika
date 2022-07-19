# 10/10
import random as rd

def TwoSum(arr):
    i = 0
    goal = arr[0]
    result = set()
    while i < len(arr) * 10:
        r1 = rd.randint(1, len(arr)-1)
        r2 = rd.randint(1, len(arr)-1)
        if arr[r1] + arr[r2] == goal:
            result.add(arr[r1])
            result.add(arr[r2])
        i += 1
    return result


print(TwoSum([7,3,5,2,-4,8,11]))

"""def TwoSum(arr):
    i = 1
    result = ""
    while i < len(arr) - 1:
        temp_num = arr[i]
        goal = arr[0] - temp_num
        if goal in arr[1:] and arr[i] != goal:
            result += f"{arr[i]},{goal} "
    if result:
        return result
    return -1"""

"""def TwoSum(arr):
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
    return -1"""
