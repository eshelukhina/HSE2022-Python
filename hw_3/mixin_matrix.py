import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class MixinMatrix:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = np.asarray(value)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.value])

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)


class MatrixExt(NDArrayOperatorsMixin, MixinMatrix):

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        for i in inputs:
            if not isinstance(i, type(self)):
                return NotImplemented
        inputs = (i.value for i in inputs)
        return type(self)(getattr(ufunc, method)(*inputs, **kwargs))
