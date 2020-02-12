import unittest


def is_unique_1(given_string):
    """
    Assumes that lowercase and uppercase letters are DIFFERENT.
    E.g. Returns True for "AaBbCc"
    """
    length_of_string = len(given_string)
    converted_set = set(given_string)
    length_of_set = len(converted_set)

    if length_of_string == length_of_set:
        print("Test string {} is UNIQUE".format(given_string))
        return True
    else:
        print("Test string {} is NOT UNIQUE".format(given_string))
        return False


def is_unique_2(given_string):
    """
    Assumes that  lowercase and uppercase letters are SAME
    E.g. Returns False for "AaBbCc"
    """

    lowered_string = given_string.lower()

    length_of_string = len(lowered_string)
    converted_set = set(lowered_string)
    length_of_set = len(converted_set)

    if length_of_string == length_of_set:
        print("Test string {} is UNIQUE".format(given_string))
        return True
    else:
        print("Test string {} is NOT UNIQUE".format(given_string))
        return False


def is_unique_3(given_string):
    """
    DO not use "set" data structure of Python
    """
    unique_char_list = []
    for item in given_string:
        if item not in unique_char_list:
            unique_char_list.append(item)
        else:
            # This char exists in the unique list
            return False

    return True


class Test(unittest.TestCase):
    test_data_true_1 = ['abcd', 's4fad', '', "AaBbCc"]
    test_data_false_1 = ['23ds2', 'hb 627jh=j ()']

    test_data_true_2 = ['abcd', 's4fad', '']
    test_data_false_2 = ['23ds2', 'hb 627jh=j ()', "AaBbCc"]

    def test_whether_unique_3(self):
        # True check
        for item in self.test_data_true_1:
            self.assertTrue(is_unique_3(item))

        # False check
        for item in self.test_data_false_1:
            self.assertFalse(is_unique_3(item))

    def test_whether_unique_1(self):
        # True check
        for item in self.test_data_true_1:
            result = is_unique_1(item)
            self.assertTrue(result)

        # False check
        for item in self.test_data_false_1:
            result = is_unique_1(item)
            self.assertFalse(result)

    def test_whether_unique_2(self):
        # True check
        for item in self.test_data_true_2:
            result = is_unique_2(item)
            self.assertTrue(result)

        # False check
        for item in self.test_data_false_2:
            result = is_unique_2(item)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()



