
# Expected result
# [
# [21, 16, 11, 6, 1],
# [22, 17, 12, 7, 2],
# [23, 18, 13, 8, 3],
# [24, 19, 14, 9, 4],
# [25, 20, 15, 10, 5]]

# 1st column becomes the first row, the row has 1st column eles in rev order. Same for all cols and rows
# O(NxN)

def matrixRotate(matrix):

    revMatrix = []
    l = len(matrix)

    for r in range(0, l):
        row = []
        for i in range(l-1, -1, -1):
            row.append(matrix[i][r])

        revMatrix.append(row)

    return revMatrix


matrix = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20],
[21, 22, 23, 24, 25]]

print(matrixRotate(matrix))
