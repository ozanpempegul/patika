def second_great_low(arr):
    result = []
    arr.sort()
    for i in arr:
        if i != arr[0]:
            result.append(i)
            break
    for i in reversed(arr):
        if i != arr[-1]:
            result.append(i)
            break
    final = f"{result[0]} {result[1]}"
    return final


# For input [80, 80] the output was incorrect. The correct output is 80 80
# iki sayı varsa ve aynıysa boş dönmeli. soru yanlış.

print(second_great_low([1, 42, 42, 180]))
