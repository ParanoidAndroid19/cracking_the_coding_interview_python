
# Solution 1: The obvious straight forward method.
# First find the index of ele that is zero. Then record the row (i) and col (j) of the element, send this to a new function.
# In the function, make a while loop:
# (while i<len and j<len):
# m[row][j] j++
# m[i][col]

#
# def zeroMatrix(matrix):
#
#     nr = len(matrix) # no of rows
#     nc = len(matrix[0])  # no of columns
#     li = []
#
#     for row in range(nr):
#         try:
#             col = matrix[row].index(0)
#             li.append([row, col])
#         except ValueError:
#             pass
#
#     for ele in li:
#         matrix = makeZero(matrix, ele[0], ele[1], nr, nc)
#
#     return matrix
#
#
# def makeZero(m, row, col, nr, nc):
#     i = 0
#     j = 0
#
#     while i < nr and j < nc:
#         m[row][j] = 0
#         m[i][col] = 0
#         i += 1
#         j += 1
#
#     while i < nr:
#         m[i][col] = 0
#         i += 1
#
#     while j < nc:
#         m[row][i] = 0
#         j += 1
#
#     return m

# expected = [
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [11, 0, 13, 14, 0],
# [0, 0, 0, 0, 0],
# [21, 0, 23, 24, 0]
# ]


# Solution 2:
# Can you reduce the additional space usage to 0(1) by using the matrix itself for data storage?
# I will append the list (list of rows and cols that have 0 in it) as the last row of the matrix.
# I won't traverse the last row, as I'll be considering the length of original matrix.

def zeroMatrix(matrix):

    nr = len(matrix) # no of rows
    nc = len(matrix[0])  # no of columns

    # last empty row of matrix, where I will later append rows and cols that have 0 in it
    matrix.append([])

    for row in range(nr):
        try:
            col = matrix[row].index(0)
            matrix[-1].append([row, col])
        except ValueError:
            pass

    for k in range(len(matrix[-1])):
        matrix = makeZero(matrix, matrix[-1][k][0], matrix[-1][k][1], nr, nc)

    matrix.pop(-1)
    return matrix


def makeZero(m, row, col, nr, nc):
    i = 0
    j = 0

    while i < nr and j < nc:
        m[row][j] = 0
        m[i][col] = 0
        i += 1
        j += 1

    # will be used when no. of rows and cols are not equal in matrix
    while i < nr:
        m[i][col] = 0
        i += 1

    while j < nc:
        m[row][i] = 0
        j += 1

    return m


matrix = [
[1, 2, 3, 4, 0],
[6, 0, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 0, 18, 19, 20],
[21, 22, 23, 24, 25]
]

print(zeroMatrix(matrix))
