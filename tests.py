from random import randint
import unittest

import numpy

from stats import Stats


class StatsTestCase(unittest.TestCase):

    def assertCloseEnough(self, a, b):
        self.assertAlmostEqual(a, b)

    def test_stats(self):
        N = 10000
        a = [randint(1, 10000) for x in xrange(N)]
        b = [randint(1, 10000) for x in xrange(N)]

        s = Stats()
        s.add_data(a)
        self.assertCloseEnough(numpy.mean(a), s.mean)
        self.assertCloseEnough(numpy.var(a, ddof=1), s.variance)
        self.assertCloseEnough(numpy.std(a, ddof=1), s.standard_deviation)

        a_b = a + b
        s_b = Stats()
        s_b.add_data(b)
        s_c = s + s_b
        self.assertCloseEnough(numpy.mean(a_b), s_c.mean)
        self.assertCloseEnough(numpy.var(a_b, ddof=1), s_c.variance)
        self.assertCloseEnough(numpy.std(a_b, ddof=1), s_c.standard_deviation)
