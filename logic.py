import random


def game(n):
    matrix = [[0] * n for _ in range(n)]
    matrix = add(matrix)
    matrix = add(matrix)
    return matrix


def add(matrix):
    x = random.randint(0, len(matrix) - 1)
    y = random.randint(0, len(matrix) - 1)
    while matrix[x][y] != 0:
        x = random.randint(0, len(matrix) - 1)
        y = random.randint(0, len(matrix) - 1)
    matrix[x][y] = 2
    return matrix


def reverse(matrix):
    new = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new[i][j] = matrix[i][len(matrix) - 1 - j]
    return new


def transpose(matrix):
    new = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new[i][j] = matrix[j][i]
    return new


def compress(matrix):
    new = [[0] * len(matrix) for _ in range(len(matrix))]
    done = False
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                new[i][count] = matrix[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done


def merge(matrix, done):
    for i in range(len(matrix)):
        for j in range(len(matrix) - 1):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                matrix[i][j] *= 2
                matrix[i][j + 1] = 0
                done = True
    return matrix, done


def game_not_over(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                return True
    for i in range(len(matrix)):
        for j in range(len(matrix) - 1):
            if matrix[i][j] == matrix[i][j + 1]:
                return True
    for i in range(len(matrix) - 1):
        for j in range(len(matrix)):
            if matrix[i + 1][j] == matrix[i][j]:
                return True
    return False


def win(matrix, number):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == number:
                return True
    return False


def get_score(matrix):
    score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            score += matrix[i][j]
    return score


def up(matrix):
    # print("Up")
    matrix = transpose(matrix)
    matrix, done = compress(matrix)
    matrix, done = merge(matrix, done)
    matrix = compress(matrix)[0]
    matrix = transpose(matrix)
    return matrix, done


def down(matrix):
    # print("Down")
    matrix = transpose(matrix)
    matrix = reverse(matrix)
    matrix, done = compress(matrix)
    matrix, done = merge(matrix, done)
    matrix = compress(matrix)[0]
    matrix = reverse(matrix)
    matrix = transpose(matrix)
    return matrix, done


def left(matrix):
    # print("Left")
    matrix, done = compress(matrix)
    matrix, done = merge(matrix, done)
    matrix = compress(matrix)[0]
    return matrix, done


def right(matrix):
    # print("Right")
    matrix = reverse(matrix)
    matrix, done = compress(matrix)
    matrix, done = merge(matrix, done)
    matrix = compress(matrix)[0]
    matrix = reverse(matrix)
    return matrix, done
