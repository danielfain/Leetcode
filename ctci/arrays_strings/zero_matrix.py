def zero_matrix(matrix):            # O(n^2) time and O(n) space
    m = len(matrix)
    n = len(matrix[0])

    zeros_seen = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zeros_seen.append((i, j))

    for tup in zeros_seen:
        set_row(matrix, tup[0])
        set_column(matrix, tup[1])

    return matrix


def set_row(matrix, row_index):
    n = len(matrix[0])

    for j in range(n):
        matrix[row_index][j] = 0


def set_column(matrix, column_index):
    m = len(matrix)

    for i in range(m):
        matrix[i][column_index] = 0


matrix = [
    [1, 2, 0, 4],
    [5, 6, 7, 8]
]

result = [
    [0, 0, 0, 0],
    [5, 6, 0, 8]
]

print(zero_matrix(matrix))