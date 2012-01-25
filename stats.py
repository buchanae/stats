import collections
import math


__version__ = '0.1'


class Stats(object):

    """TODO"""

    def __init__(self):
        self.mean = 0.0
        self.ssr = 0.0
        self.n = 0.0

    def add_data(self, data):
        """TODO"""

        if not isinstance(data, collections.Iterable):
            data = [data]

        for value in data:
            self.n += 1
            delta = value - self.mean
            self.mean += delta / self.n
            self.ssr += delta * (value - self.mean)

    @property
    def variance(self):
        if self.n > 0:
            return self.ssr / (self.n - 1)
        else:
            return 0.0

    @property
    def standard_deviation(self):
        return math.sqrt(self.variance)

    def __add__(self, other):
        """TODO"""

        if not isinstance(other, Stats):
            s = 'unsupported operand type(s) for +: {} and {}'
            raise TypeError(s.format(type(self), type(other)))
        else:
            s = Stats()
            s.n = self.n + other.n
            d = other.mean - self.mean
            s.mean = (self.n * self.mean + other.n * other.mean) / (self.n + other.n)
            s.ssr = self.ssr + other.ssr + d**2 * (self.n * other.n / s.n)
            return s

    def __str__(self):
        s = 'Mean: {}, Standard Deviation: {}, Variance: {}, N: {}'
        return s.format(self.mean, self.standard_deviation, self.variance, self.n)
