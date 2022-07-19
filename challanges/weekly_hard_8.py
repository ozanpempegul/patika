import numpy as np
def convert_to_list(s):
    string_list = list(s)
    string_list.remove("(")
    string_list.remove(")")
    for i in range(string_list.count(",")):
        string_list.remove(",")
    return string_list
def SudokuQuadrantChecker(str_arr):
    rows = []
    illegal_quadrants = list()
    for i in str_arr:
        row = convert_to_list(i)
        rows.append(row)
    columns = []
    A = np.array(rows)
    i = 0
    while i < len(A):
        column = []
        for j in A[:, i]:
            column.append(j)
        columns.append(column)
        i += 1
    i = 0  # row
    current_quadrant = 1
    while i < len(rows):
        j = 0  # column
        while j < len(rows[i]):
            if rows[i].count(rows[i][j]) > 1 and rows[i][j] != "x":
                if j > 5:
                    illegal_quadrants.append(current_quadrant + 2)
                elif j > 2:
                    illegal_quadrants.append(current_quadrant + 1)
                else:
                    illegal_quadrants.append(current_quadrant)
            j += 1
        i += 1
        if i % 3 == 0 and i > 0:
            current_quadrant += 3
    i = 0  # column
    current_quadrant = 1
    while i < len(columns):
        j = 0  # row
        while j < len(columns[i]):
            if columns[i].count(columns[i][j]) > 1 and columns[i][j] != "x":
                if j > 5:
                    illegal_quadrants.append(current_quadrant + 6)
                elif j > 2:
                    illegal_quadrants.append(current_quadrant + 3)
                else:
                    illegal_quadrants.append(current_quadrant)
            j += 1
        i += 1
        if i % 3 == 0 and i > 0:
            current_quadrant += 1
    result = ""
    illegal_quadrants.sort()
    for i in illegal_quadrants:
        if str(i) not in result:
            result += str(i) + ","
    if result:
        return result.strip(",")
    return "legal"

print(SudokuQuadrantChecker(["(1,2,3,4,5,6,7,8,9)","(x,x,x,x,x,x,x,x,x)","(6,x,5,x,3,x,x,4,x)","(2,x,1,5,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,8)"]))

# 1. For input ["(1,2,3,4,5,6,7,8,9)","(x,x,x,x,x,x,x,x,x)","(6,x,5,x,3,x,x,4,x)","(2,x,1,5,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,8)"] the output was incorrect. The correct output is legal
#
# 2. For input ["(1,2,3,4,5,6,7,8,9)","(x,x,x,x,x,x,x,x,x)","(6,x,5,x,3,x,x,4,x)","(2,x,1,5,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,4)","(9,1,2,3,4,5,6,7,8)"] the output was incorrect. The correct output is legal
#
# 3. For input ["(1,2,3,4,5,6,7,8,9)","(4,5,6,x,x,x,x,x,x)","(7,8,9,x,x,x,x,x,x)","(2,3,4,x,x,x,x,x,x)","(5,6,7,x,x,x,x,x,x)","(8,9,1,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,1)"]
