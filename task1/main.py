import unittest


def logical_negation(num):
    return (int(num) ^ 1) & 1


class TestLogicalNegation(unittest.TestCase):

    def test_positive_zero(self):
        """Test negation of 0."""
        self.assertEqual(logical_negation(0), 1)

    def test_positive_one(self):
        """Test negation of 1."""
        self.assertEqual(logical_negation(1), 0)

    def test_negative_number(self):
        """Test negation of a negative number."""
        self.assertEqual(logical_negation(-5), 0)

    def test_positive_even(self):
        """Test negation of a positive even number."""
        self.assertEqual(logical_negation(10), 1)

    def test_positive_odd(self):
        """Test negation of a positive odd number."""
        self.assertEqual(logical_negation(11), 0)

    def test_none(self):
        """Test None input."""
        with self.assertRaises(TypeError):
            logical_negation(None)


if __name__ == "__main__":
    # num = int(input("Enter a number: "))
    # result = logical_negation(num)
    # print("Logical negation of", num, "is", result)
    unittest.main()
