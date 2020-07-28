def rotate_matrix(matrix):              # O(n^2) time and O(n^2) space
    n = len(matrix)

    new_matrix = [[i+1 for i in range(n)] for _ in range(n)]

    for i in range(n):
        nums = matrix[i]
        for j in range(n):
            new_matrix[j][n-i-1] = nums[j]

    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_matrix(matrix))

# TODO O(1) space implementation