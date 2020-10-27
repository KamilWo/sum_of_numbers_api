import unittest

from app.utils import sum_of_numbers


class TestStringMethods(unittest.TestCase):

    def test_sum_of_numbers(self):
        """ Testing sum of numbers helper function. """

        n_list = [1, 2, 4, 6]
        assert 13 == sum_of_numbers(n_list)

        m_list = list(range(1000))

        assert 499500 == sum_of_numbers(m_list)

        b_list = [1, 'a']

        with self.assertRaises(Exception):
            sum_of_numbers(b_list)
