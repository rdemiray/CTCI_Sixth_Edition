"""
Swap 2 numbers without using temp variable
"""
import unittest


def swap_two_numbers(num_1, num_2):
    """

    :param num_1:
    :param num_2:
    :return:
    """

    # Difference between the 2 numbers AND one of the numbers are enough to reconstruct the other number
    # Keep one of the numbers and the diff always intact during swapping operation

    num_2 = num_2 - num_1  # num_2 now holds the diff info and num_1 is intact
    num_1 = num_1 + num_2  # Diff + num_1 is equal to num_2, we assign it to num_1 to swap it
    num_2 = num_1 - num_2

    return num_1, num_2


class TestClass(unittest.TestCase):

    test_data = [
        ((3, 5), (5, 3)),
        ((5, 3), (3, 5)),
        ((0, 5), (5, 0)),
        ((5, 0), (0, 5)),
        ((5, -3), (-3, 5)),
        ((-5, 3), (3, -5)),
        ((3, 0), (0, 3)),
    ]

    def test_method(self):

        for data in self.test_data:
            self.assertEqual(
                swap_two_numbers(data[0][0], data[0][1]),
                data[1],
                msg=f"Test failed for the test dataset of: {data}"
            )


if __name__ == "__main__":
    unittest.main()