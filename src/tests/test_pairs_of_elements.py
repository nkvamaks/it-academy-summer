import ddt
from homework6.pairs_of_elements import pairs_elem
import unittest


@ddt.ddt
class TestPairs(unittest.TestCase):

    @ddt.data(
        ('1 1', 1),
        ('1 1 1', 3),
        ('1 1 1 1', 6),
        ('1 abc ,."qw 1 ku 1 42 1', 6),
        ('1 2 blabla 2 1 q 1 ,,,., 1', 7),
        ('123 234 123 234 foo foo bar spam 42 42 42', 6),
        ('', 0),
        ('1', 0),
    )
    @ddt.unpack
    def test_pairs_elem(self, string, expected):
        """String '{}' expected {} pairs."""
        result = pairs_elem(string)
        self.assertEqual(result, expected)

    @ddt.data(
        [1, 2, 2],
        ('a', 'a'),
        {'x': 1, 'foo': 22},
        {1, 'e', '5'},
        None,
        )
    def test_pairs_elem_input_not_string(self, input_value):
        with self.assertRaises(AttributeError):
            pairs_elem(input_value)
