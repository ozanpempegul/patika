def histogram_area(arr):
    areas = []
    i = 0
    while i < len(arr) - 1:
        temp_area = arr[i]

        # check forward
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[i]:
                areas.append(temp_area)
                break
            else:
                temp_area += arr[i]
                if j == len(arr) - 1:
                    areas.append(temp_area)
            j += 1

        # check reverse
        k = i - 1
        while k >= 0:
            if arr[k] < arr[i]:
                break
            else:
                areas[i] += arr[i]
            k -= 1
        i += 1
    return max(areas)


print(histogram_area([6, 3, 1, 4, 12, 4]))
print(histogram_area([5, 6, 7, 4, 1]))
print(histogram_area([12]))
