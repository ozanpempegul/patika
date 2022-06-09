# 10/10
def most_frequent(arr):
    counter = [1, -1]  # counter[0] count of most frequent number, counter[1] number itself
    for i in arr:
        if arr.count(i) > counter[0]:
            counter[0] = arr.count(i)
            counter[1] = i

    return counter[1]


a = [1, 3, 2, 4, 5]
print(most_frequent(a))
