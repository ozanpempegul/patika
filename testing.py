def f(a):
    n = int(a[0])
    temp = a[1]
    current_step = 0
    end = a[n]
    steps_array = []
    first_letters = []
    second_letters = []
    path = [a[1]]
    repeat = 0
    temp_index = 0
    for i in range(n + 1, len(a)):
        index_of_second = a.index(a[i][2])
        index_of_first = a.index(a[i][0])
        current_step = index_of_second - index_of_first
        steps_array.append(current_step)
        first_letters.append(a[i][0])
        second_letters.append(a[i][2])

    while repeat <= len(a) - n:
        for i in range(len(first_letters)):
            if first_letters[i] == temp and steps_array[i] >= current_step:
                temp_index = i
        path.append(second_letters[temp_index])
        temp = second_letters[temp_index]
        if temp == end:
            return "-".join(path)
        current_step = 0
        repeat += 1

    return "-".join(path)


print(f(["4","X","Y","Z","W","X-Y","Y-Z","X-W"]))

