# 15/15

def TransitivityRelations(strArr):

    def addConnections(node1, node2):
        i = 0
        while i < len(connections[node2]):
            if connections[node2][i] == 1 and connections[node1][i] == 0 and node1 != i:
                connections[node1][i] = 1
                result.append(f"({node1},{i})")
            i += 1

    def stringsToArrays(element):
        result = []
        i = 1
        while i < len(element):
            result.append(int(element[i]))
            i += 2
        return result


    connections = []
    result = []

    for i in strArr:
        connections.append(stringsToArrays(i))

    i = 0
    while i < len(connections):
        j = 0
        while j < len(connections[i]):
            if j != i and connections[i][j] == 1:
                addConnections(i, j)
            j += 1
        i += 1

    if len(result) == 0:
        return "transitive"

    result.sort()
    return "-".join(result)


print(TransitivityRelations(["(1,1,1)", "(0,1,1)", "(0,1,1)"]))
print(TransitivityRelations(["(0,1,0,0)", "(0,0,1,0)", "(0,0,1,1)", "(0,0,0,1)"]))
