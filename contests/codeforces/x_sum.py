def bottomRight(row, col):
    if (row, col) in memoBottomRight:
        return memoBottomRight[(row, col)]
    if row < 0 or col >= len(grid[0]):
        return 0
    memoBottomRight[(row, col)] = grid[row][col] + bottomRight(row - 1, col + 1)
    return memoBottomRight[(row, col)]
     
    
def bottomLeft(row, col):
    if (row, col) in memoBottomLeft:
        return memoBottomLeft[(row, col)]
    if row < 0 or col < 0:
        return 0
    memoBottomLeft[(row, col)] = grid[row][col] + bottomLeft(row - 1, col - 1)
    return memoBottomLeft[(row, col)]
         
def topRight(row, col):
    if (row, col) in memoTopRight:
        return memoTopRight[(row, col)]
    if row >= len(grid) or col >= len(grid[0]):
        return 0
    memoTopRight[(row, col)] = grid[row][col] + topRight(row + 1, col + 1)
    return memoTopRight[(row, col)]
     
def topLeft(row, col):
    if (row, col) in memoTopLeft:
        return memoTopLeft[(row, col)]
    if row  >= len(grid) or col < 0:
        return 0
    memoTopLeft[(row, col)] = grid[row][col] + topLeft(row + 1, col - 1)
    return memoTopLeft[(row, col)]

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    grid = []
    memoBottomRight = {}
    memoBottomLeft = {}
    memoTopRight = {}
    memoTopLeft = {}
    for _ in range(N):
        nums = list(map(int, input().split()))
        grid.append(nums)
    maxScore = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            maxScore = max(maxScore, grid[row][col]\
                            + bottomRight(row - 1,col + 1) \
                            + bottomLeft(row - 1,col - 1) \
                            + topRight(row + 1, col + 1) \
                            + topLeft(row + 1, col - 1))
    
    print(maxScore) 
