import random


class Logic:
    def __init__(self, n):
        self.n = n
        self.score = 0
        self.matrix = [[0] * n for _ in range(n)]
        self.add()
        self.add()

    def add(self):
        x = random.randint(0, self.n - 1)
        y = random.randint(0, self.n - 1)
        while self.matrix[x][y] != 0:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
        self.matrix[x][y] = 2

    def reverse(self):
        new = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                new[i][j] = self.matrix[i][self.n - 1 - j]
        self.matrix = new

    def transpose(self):
        new = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                new[i][j] = self.matrix[j][i]
        self.matrix = new

    def compress(self):
        new = [[0] * self.n for _ in range(self.n)]
        done = False
        for i in range(self.n):
            count = 0
            for j in range(self.n):
                if self.matrix[i][j] != 0:
                    new[i][count] = self.matrix[i][j]
                    if j != count:
                        done = True
                    count += 1
        self.matrix = new
        return done

    def compress_row0(self):
        new_row = [0] * self.n
        done = False
        count = 0
        for j in range(self.n):
            if self.matrix[0][j] != 0:
                new_row[count] = self.matrix[0][j]
                if j != count:
                    done = True
                count += 1

        self.matrix[0] = new_row
        return done

    def merge(self, done):
        for i in range(self.n):
            for j in range(self.n - 1):
                if self.matrix[i][j] == self.matrix[i][j + 1] and self.matrix[i][j] != 0:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]
                    done = True
        return done

    def game_not_over(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == 0:
                    return True
        for i in range(self.n):
            for j in range(self.n - 1):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        for i in range(self.n - 1):
            for j in range(self.n):
                if self.matrix[i + 1][j] == self.matrix[i][j]:
                    return True
        return False

    def win(self, number):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == number:
                    return True
        return False

    def up(self):
        self.transpose()
        done = self.compress()
        done = self.merge(done)
        self.compress_row0()
        self.transpose()
        return done

    def down(self):
        self.transpose()
        self.reverse()
        done = self.compress()
        done = self.merge(done)
        self.compress_row0()
        self.reverse()
        self.transpose()
        return done

    def left(self):
        done = self.compress()
        done = self.merge(done)
        done = self.compress_row0()
        return done

    def right(self):
        self.reverse()
        done = self.compress()
        done = self.merge(done)
        self.compress_row0()
        self.reverse()
        return done
