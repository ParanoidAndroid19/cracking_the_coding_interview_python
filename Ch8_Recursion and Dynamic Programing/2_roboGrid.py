def path(cell):

    [r,c] = cell

    # destination is the bottom right-most cell
    if cell == [row-1,col-1]:
        return "Path Found"

    # right move
    elif ([r, c+1] not in obstacles) and (r<row) and (c+1<col):
        print([r, c+1])
        return path([r, c+1])

    # down move
    elif ([r+1, c] not in obstacles) and (r+1<row) and (c<col):
        print([r+1, c])
        return path([r+1, c])

    else:
        return "Path not Found"


row = 5
col = 4
grid = []

for i in range(0, row):
    for j in range(0,col):
        grid.append([i,j])

obstacles = [[2,1], [0,3]]

print(grid)

print(path([0,0]))
