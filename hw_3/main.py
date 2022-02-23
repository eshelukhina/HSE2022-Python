import numpy as np

from matrix import Matrix
from mixin_matrix import MatrixExt


def easy():
    easy_and_medium_write_to_files(
        Matrix(np.random.randint(0, 10, (10, 10))),
        Matrix(np.random.randint(0, 10, (10, 10))),
        'easy'
    )


def medium():
    easy_and_medium_write_to_files(
        MatrixExt(np.random.randint(0, 10, (10, 10))),
        MatrixExt(np.random.randint(0, 10, (10, 10))),
        'medium'
    )


def easy_and_medium_write_to_files(m1, m2, level):
    with open(f'artifacts/{level}/matrix+.txt', 'w') as f:
        f.write((m1 + m2).__str__())
    with open(f'artifacts/{level}/matrix*.txt', 'w') as f:
        f.write((m1 * m2).__str__())
    with open(f'artifacts/{level}/matrix@.txt', 'w') as f:
        f.write((m1 @ m2).__str__())


def hard():
    a = Matrix([[2, 3], [9, 4]])
    c = Matrix([[8, 6], [3, 1]])
    b = Matrix([[1, 2], [3, 4]])
    d = Matrix([[1, 2], [3, 4]])
    ab = a @ b
    c._mul_cache = {}
    cd = c @ d
    with open('artifacts/hard/A.txt', 'w') as f:
        f.write(a.__str__())
    with open('artifacts/hard/B.txt', 'w') as f:
        f.write(b.__str__())
    with open('artifacts/hard/C.txt', 'w') as f:
        f.write(c.__str__())
    with open('artifacts/hard/D.txt', 'w') as f:
        f.write(d.__str__())
    with open('artifacts/hard/AB.txt', 'w') as f:
        f.write(ab.__str__())
    with open('artifacts/hard/CD.txt', 'w') as f:
        f.write(cd.__str__())
    with open('artifacts/hard/hash.txt', 'w') as fp:
        fp.write("Hash AB: " + str(ab.__hash__()) + '\n' + "Hash CD: " + str(cd.__hash__()))


if __name__ == '__main__':
    np.random.seed(0)
    easy()
    medium()
    hard()
