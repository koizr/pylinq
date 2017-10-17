import unittest
from pylinq import Enumerable


class TestEnumerable(unittest.TestCase):
    def test_init(self):
        actual = list(Enumerable([1, 2, 3]))
        expected = [1, 2, 3]
        self.assertListEqual(actual, expected)

    def test_from(self):
        actual = list(Enumerable.from_([1, 2, 3]))
        expected = [1, 2, 3]
        self.assertListEqual(actual, expected)

    def test_range(self):
        actual = list(Enumerable.range(5, 10, 2))
        expected = [x for x in range(5, 10, 2)]
        self.assertListEqual(actual, expected)

    def test_where(self):
        actual = list(Enumerable.from_([1, 2, 3, 4, 5]).where(lambda x: x % 2 == 0))
        expected = [2, 4]
        self.assertListEqual(actual, expected)

    def test_select(self):
        actual = list(Enumerable.from_([1, 2, 3]).select(lambda x: x * 5))
        expected = [5, 10, 15]
        self.assertListEqual(actual, expected)

    def test_all(self):
        all_true = Enumerable.from_([True, 1, [''], 'x']).all()
        self.assertTrue(all_true)

        has_false = Enumerable.from_([False, 1, [''], 'x']).all()
        self.assertFalse(has_false)

        all_true = Enumerable.from_([1, 2, 3, 4]).all(lambda x: x < 5)
        self.assertTrue(all_true)

        has_false = Enumerable.from_([1, 2, 3, 4, 5]).all(lambda x: x < 5)
        self.assertFalse(has_false)


if __name__ == '__main__':
    unittest.main()
