# 5 / ?
def ShortestPath(a):
    n = int(a[0])
    temp = a[1]
    current_step = 0
    end = a[n]
    steps_array = []
    first_elements = []
    second_elements = []
    path = [a[1]]
    repeat = 0
    temp_index = 0
    for i in range(n + 1, len(a)):
        index_of_second = a.index(a[i].split("-")[1])
        index_of_first = a.index(a[i].split("-")[0])
        current_step = index_of_second - index_of_first
        steps_array.append(current_step)
        first_elements.append(a[i].split("-")[0])
        second_elements.append(a[i].split("-")[1])

    print(first_elements, second_elements, steps_array)

    while repeat <= len(a) - n:
        for i in range(len(first_elements)):
            print(first_elements[i], temp, second_elements[i])
            if first_elements[i] == temp and steps_array[i] >= current_step:
                temp_index = i

        path.append(second_elements[temp_index])
        temp = second_elements[temp_index]


        if temp == end:
            return "-".join(path)
        current_step = 0
        repeat += 1
        print("------------------------")

    return -1


print(ShortestPath())

"""
Given input: ["4","X","Y","Z","W","X-Y","Y-Z","X-W"] it was correct.

1. For input ["6","A","B","C","Z","Y","Q","B-C","A-B","A-Z","C-Y","Z-Y","C-Q"] the output was incorrect. The correct output is A-B-C-Q

2. For input ["6","Z","B","C","A","Y","Q","B-C","A-B","A-Z","C-Y","Z-Y","C-Q"] the output was incorrect. The correct output is Z-Y-C-Q

3. For input ["5","c","h","d","s","m","c-s","s-h","d-m","h-d"] the output was incorrect. The correct output is c-s-h-d-m

4. For input ["2","First Street","Third Street"] the output was incorrect. The correct output is -1

5. For input ["7","D","A","N","I","E","L","B","D-A","A-N","E-B","E-L"] the output was incorrect. The correct output is -1

6. For input ["9","Z","B","C","D","R","A","Y","Q","E","A-Z","A-R","Z-Y","Z-C","C-B","Y-Q","Q-D","D-E","R-E"] the output was incorrect. The correct output is Z-A-R-E

7. For input ["5","N1","N2","N3","N4","N5","N1-N3","N3-N4","N4-N5","N5-N2","N2-N1"] the output was incorrect. The correct output is N1-N2-N5
"""