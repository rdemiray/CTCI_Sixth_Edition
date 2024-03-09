import unittest


def is_organized_number(number):
    """
    Checks if the given number is organized number
    40585 = 4! + 0! + 5! + 8! + 5!
    145 = 1! + 4! + 5!

    :param number:
    :return:
    """

    string_form = str(number)
    sum = 0

    for num in string_form:
        sum += factorial(int(num))

    if sum == number:
        # Organized number
        # print(f"{number} is a organized number")
        return True
    else:
        # Not organized number
        # print(f"{number} is NOT an organized number")
        return False


def factorial(number):
    """

    :param number:
    :return:
    """
    if number < 0:
        print("Please enter a positive integer or ZERO")
        return False

    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


def find_all_organized_numbers(number):
    """

    :param number:
    :return:
    """

    list_of_all_organized_numbers = []

    for i in range(number):
        if is_organized_number(i):
            list_of_all_organized_numbers.append(i)

    # Print all organized numbers to the console and then return the list to get asserted

    for item in list_of_all_organized_numbers:
        print("{} is an organized number \n".format(item))

    return list_of_all_organized_numbers


# find_all_organized_numbers(40586)


class TestClass(unittest.TestCase):
    test_data = [
        (1, True),
        (2, True),
        (145, True),
        (40585, True),
        (100, False),
        (10, False)
    ]

    test_data_2 = [
        (40586, [1, 2, 145, 40585])
    ]

    test_data_3 = [
        (3, 6),
        (2, 2),
        (1, 1),
        (0, 1),
        (5, 120),
        (4, 24),
        (-1, False)
    ]

    def test_method(self):
        """

        :return:
        """

        # Unit tests for the method "is_organized_number()"
        for item in self.test_data:
            self.assertEqual(
                is_organized_number(item[0]),
                item[1],
                msg=f"{item[0]} is an organized number? {item[1]}")

        # Unit test for the method "find_all_organized_numbers()"
        for item in self.test_data_2:
            self.assertEqual(
                find_all_organized_numbers(item[0]),
                item[1],
                msg="Assertion failed")

        # Unit tests for the method "factorial()"
        for item in self.test_data_3:
            self.assertEqual(
                factorial(item[0]),
                item[1],
                msg=f"{item[0]}! is not equal to {item[1]}!")
