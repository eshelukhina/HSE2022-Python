from mixin_matrix import MixinMatrix


class MulMixin:
    def __init__(self):
        self._matrix = None

    def __hash__(self):
        return sum(map(sum, self._matrix)) % (10 ** 9 + 7)


class Matrix(MulMixin, MixinMatrix):
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    @staticmethod
    def valid_matrix(matrix):
        for m in matrix:
            if len(m) != len(matrix[0]):
                raise ValueError("Invalid Dimension")

    def cmp_matrix(self, other):
        if (self.m != other.m) or (self.n != other.n):
            raise Exception("Invalid Dimensions")

    def check_validation(self, other):
        self.valid_matrix(other.matrix)
        self.cmp_matrix(other)

    def __init__(self, size):
        super().__init__()
        self.valid_matrix(size)
        self._matrix = []
        for m in size:
            self._matrix.append(m)
        self._mul_cache = {}
        self.n = len(self._matrix)
        self.m = len(self._matrix[0])

    def __add__(self, other):
        res = []
        self.check_validation(other)
        for m, i in zip(other.matrix, range(other.n)):
            res.append([m[j] + self._matrix[i][j] for j in range(len(m))])
        return Matrix(res)

    def __mul__(self, other):
        res = []
        self.check_validation(other)
        for m, i in zip(other.matrix, range(other.n)):
            res.append([m[j] * self._matrix[i][j] for j in range(len(m))])
        return Matrix(res)

    def __matmul__(self, other):
        self.check_validation(other)
        key = self.__hash__(), other.__hash__()
        if key in self._mul_cache:
            return self._mul_cache[key]
        res = [[sum(i * j for i, j in zip(row, col)) for col in list(zip(*other.matrix))] for row in self._matrix]
        self._mul_cache[key] = Matrix(res)
        return Matrix(res)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self._matrix])
