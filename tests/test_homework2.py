from string import punctuation

import ddt
import unittest


from src.homework2.task1 import total_sum
from src.homework2.task2 import longest_word
from src.homework2.task3 import sub_string
from src.homework2.task4 import count_letters
from src.homework2.task5 import fibonacci
from src.homework2.task6 import palindrom


@ddt.ddt
class TestHomework2(unittest.TestCase):

    @ddt.data(
        (10, 33, 400, '4132 rubles 0 kopecks'),
        (50, 50, 50, '2525 rubles 0 kopecks'),
        (23, 36, 111, '2592 rubles 96 kopecks'),
        (535, 14, 543, '290581 rubles 2 kopecks'),
        (0, 0, 543, '0 rubles 0 kopecks'),
        (12, 12, 0, '0 rubles 0 kopecks'),
        (1, 0, 5, '5 rubles 0 kopecks'),
        (0, 5, 5, '0 rubles 25 kopecks'),
    )
    @ddt.unpack
    def test_task1(self, m, n, s, expected):
        """Task1. Roubles: {}, kopecks: {}, number: {}"""
        self.assertEqual(total_sum(m, n, s), expected)

    @ddt.data(
        ("", ""),
        (punctuation, ""),
        ("{} word wordd".format(punctuation), "wordd"),
        ("word wordd {} ".format(punctuation), "wordd"),
        ("word {} wordd  ".format(punctuation), "wordd"),
        (" {}    {}  ".format(punctuation, punctuation), ""),
        ("{} wordddd {} wordd  ".format(punctuation, punctuation), "wordddd"),
        ("word            wordd", "wordd"),
    )
    @ddt.unpack
    def test_task2(self, str_, expected):
        """Task2. String: {}, expected: {}"""
        self.assertEqual(longest_word(str_), expected)

    @ddt.data(
        ("", ""),
        (punctuation, punctuation),
        ("abc cde def", "abcdef"),
        ("asdfasdfadsf           s fd", "asdf"),
        ("word {} wordd  ".format(punctuation), "word{}".format(punctuation)),
        (" {}    {}  ".format(punctuation, punctuation), punctuation),
        ("           ", ""),
        ("word            wordd", "word"),
    )
    @ddt.unpack
    def test_task3(self, str_, expected):
        """Task3. String: {}, expected: {}"""
        self.assertEqual(sub_string(str_), expected)

    @ddt.data(
        ("", (0, 0)),
        (punctuation, (0, 0)),
        ("abc cde def", (9, 0)),
        ("aASDFGASsf           s fd", (6, 7)),
        ("word {} wordd  ".format(punctuation), (9, 0)),
        ("9867565443789ASDFS{}DGSDFGSFDG sdf g".format(punctuation), (4, 15)),
        ("AAAAAAAAAA", (0, 10)),
    )
    @ddt.unpack
    def test_task4(self, str_, expected):
        """Task4. String: {}, expected: {}"""
        self.assertEqual(count_letters(str_), expected)

    @ddt.data(
        (1, 1),
        (2, 1),
        (5, 5),
        (20, 6765),
    )
    @ddt.unpack
    def test_task5(self, str_, expected):
        """Task5. Number: {}, expected: {}"""
        self.assertEqual(fibonacci(str_), expected)

    @ddt.data(
        (0, True),
        (121, True),
        (123, False),
        (1234567890987654321, True),
        (12344321, True),
        (1232, False),
        (2311323, False),
    )
    @ddt.unpack
    def test_task6(self, n, expected):
        """Task6. Number: {}, expected: {}"""
        self.assertEqual(palindrom(n), expected)


if __name__ == '__main__':
    unittest.main()
