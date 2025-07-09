import unittest


def binary_to_decimal(binary_num: str) -> int:
    """
    Binary to decimal converter using loop

    :param binary_num: Binary representation of a number in string form i.e. "0101010101"
    :return:
    """
    index = 0
    decimal_num = 0

    size = len(binary_num)
    while index < len(binary_num):
        decimal_num += int(binary_num[size - 1 - index]) * pow(2, index)
        index += 1

    print(f"Binary number {binary_num} corresponds to {decimal_num} in decimal")
    return decimal_num


def binary_to_decimal_2(binary_num: str) -> int:
    """

    :param binary_num:
    :return:
    """
    # From left to right, from the highest order to the lowest order
    index = len(binary_num) - 1

    decimal_num = 0

    for binary_digit in binary_num:
        binary_digit = int(binary_digit)

        decimal_num = decimal_num + pow(2, index) * binary_digit
        index -= 1

    print(f"Binary number {binary_num} corresponds to {decimal_num} in decimal")
    return decimal_num

def binary_to_decimal_3(binary_str):
    """
    Convert binary string to decimal manually without using int() or other built-ins.
    """
    decimal = 0
    power = len(binary_str) - 1

    for bit in binary_str:
        if bit not in ('0', '1'):
            raise ValueError("Invalid binary digit found.")
        if bit == '1':
            decimal += 2 ** power
        power -= 1

    return decimal

def binary_to_decimal_4(binary_str):
    decimal = 0
    power = 0

    reversed_binary_string = binary_str[::-1]


    for digit in reversed_binary_string:
        if digit not in ['0', '1']:
            raise ValueError('Invalid digit')

        if digit == '1':
            decimal += 2 ** power
        
        power += 1
    
    return decimal

class TestClass(unittest.TestCase):

    test_data = [
        ("01", 1),
        ("10", 2),
        ("11", 3),
        ("00000111", 7),
        ("0", 0),
        ("00000000", 0),
    ]

    def test_method(self):
        for data in self.test_data:
            self.assertEqual(binary_to_decimal(data[0]), data[1])
            self.assertEqual(binary_to_decimal_2(data[0]), data[1])
            self.assertEqual(binary_to_decimal_3(data[0]), data[1])
    
    def test_method2(self):
        for data in self.test_data:
            self.assertEqual(binary_to_decimal_4(data[0]), data[1])


if __name__ == "__main__":
    unittest.main()
