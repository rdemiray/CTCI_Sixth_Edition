import unittest


def check_if_palindrome_string(string: str) -> bool:
    """

    :param string:
    :return:
    """
    # convert everything into lowercase and remove space chars in the given string
    string = string.lower().replace(" ", "")

    # Iterate over the given string in the opposite order
    pointer = 0
    for i in reversed(string):
        if i != string[pointer]:
            return False
        pointer += 1

    return True


def check_if_palindrome_string_2(string: str) -> bool:
    """

    :param string:
    :return:
    """

    updated_string = string.lower().replace(" ", "")

    num_of_iteration = len(updated_string) // 2  # Floor division.... i.e. 5//2 = 2 , 4//2 = 2

    lower_index = 0
    upper_index = len(updated_string) - 1

    for _ in range(num_of_iteration):
        if updated_string[lower_index] != updated_string[upper_index]:
            return False
        lower_index += 1
        upper_index -= 1

    return True


class TestClass(unittest.TestCase):
    test_data = [
        ("Madam", True),
        ("Bob", True),
        ("Was it a cat I saw", True),
        ("Remi", False)
    ]

    def test_method(self):

        for data in self.test_data:
            self.assertEqual(
                check_if_palindrome_string(data[0]),
                data[1],
                msg=f"Test failed for the test dataset of: {data}"
            )

    def test_method_2(self):

        for data in self.test_data:
            self.assertEqual(
                check_if_palindrome_string_2(data[0]),
                data[1],
                msg=f"Test failed for the test dataset of: {data}"
            )


if __name__ == "__main__":
    unittest.main()

