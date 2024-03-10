"""
    A Kaprekar number is a number whose square when divided into two parts and such that sum of parts is equal
    to the original number and none of the parts has value 0

    (9)^2 = 81 ,                                      8 + 1 = 9 ;
    (45)^2 = 2025 ,                                20 + 25 = 45 ;
    (297)^2 = 88209 ,                            88 + 209 = 297 ;
    (4879)^2 = 23804641 ,                    238 + 4641 = 4879 ;
    (17344)^2 = 300814336 ,                3008 + 14336 = 17344 ;
    (538461)^2 = 289940248521 ,        289940 + 248521 = 538461 .

    There are infinitely many Kaprekar numbers and first few of them are 1, 9, 45, 55, 99,
    297, 703, 999, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999

"""
import unittest


def is_kaprekar_number(num):
    """
    Returns true if n is a Kaprekar number, else false

    :param num:
    :return:
    """
    string_num = str(num**2)

    # Index that we split string representation of a number into 2, '//' does floor division
    split_index = len(string_num)//2

    left_string = string_num[:split_index]  # First half of the string
    right_string = string_num[split_index:]  # Second half of the string

    left_num = int(left_string) if left_string != '' else 0
    right_num = int(right_string) if right_string != '' else 0

    if num == left_num + right_num:
        return True
    return False


def is_kaprekar_number_2(num):
    """
    ChatGPT generated one

    :param num:
    :return:
    """
    # Square the number
    square = num * num

    # Convert the square to a string to manipulate digits
    square_str = str(square)

    # Check if the square has only one digit, if yes return True
    if len(square_str) == 1:
        return int(square_str) == num

    # Iterate through possible split positions
    for i in range(1, len(square_str)):
        # Split the square into two parts
        left_part = int(square_str[:i])
        right_part = int(square_str[i:])

        # Check if the split parts sum up to the original number
        if left_part + right_part == num:
            return True

    return False


class TestClass(unittest.TestCase):
    test_data = [
        (55, True),
        (99, True),
        (297, True),
        (81, False),
        (1, True),
        (2, False),
        (5, False)
    ]

    def test_method(self):
        for data in self.test_data:
            self.assertEqual(
                is_kaprekar_number(data[0]),
                data[1],
                msg=f"Test failed for the test dataset of: {data}"
            )

    def test_method_2(self):
        for data in self.test_data:
            self.assertEqual(
                is_kaprekar_number_2(data[0]),
                data[1],
                msg=f"Test failed for the test dataset of: {data}"
            )


if __name__ == "__main__":
    unittest.main()
