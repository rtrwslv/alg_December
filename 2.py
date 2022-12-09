def closedIsland(matrix):
    rows = len(matrix)
    colums = len(matrix[0])
    def check(i, j):
        if not(i < 0 or j < 0 or i == rows or j == colums):
            if matrix[i][j] == 1:
                return 1
            matrix[i][j] = 1
            top = check(i - 1, j)
            bottom = check(i + 1, j)
            right = check(i, j + 1)
            left = check(i, j - 1)
            if top and bottom and right and left:
                return 1
            else:
                return 0
        
    count = 0
    for i in range(rows):
        for j in range(colums):
            if matrix[i][j] == 0:
                result = check(i, j)
                if result != float("inf"):
                    count += result
    if count == float("inf"):
        return 0
    return count
print(closedIsland([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]))