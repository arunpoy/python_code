def searchMatrix(matrix,target):
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    low = 0
    high = (m * n) - 1
    while low <= high:
        mid = (low + high) // 2
        r = mid//n
        c = mid %n
        midElement = matrix[r][c]
        print(r)
        print(c)
        if midElement == target:
            print(matrix[r][c])
            return [r][c]

        elif midElement > target:
            high = mid - 1
        else:
            low = mid + 1
    return [-1,-1]

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(searchMatrix(matrix,50))