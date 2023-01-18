 matrix = [['a', 'b', 'c', 'd', 'e'],
              ['f', 'g', 'h', 'i', 'k'],
              ['l', 'm', 'n', 'o', 'p'],
              ['q', 'r', 's', 't', 'u'],
              ['v', 'w', 'x', 'y', 'z']]
    columnMatrix = [[], [], [], [], []]
    for i in range(len(matrix)):
        columnMatrix[0].append(matrix[i][0])
        columnMatrix[1].append(matrix[i][1])
        columnMatrix[2].append(matrix[i][2])
        columnMatrix[3].append(matrix[i][3])
        columnMatrix[4].append(matrix[i][4])

    print(columnMatrix)