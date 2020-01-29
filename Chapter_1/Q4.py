import unittest


def is_palindrome_permutation(test_string):
    """
    Assumption: Incoming string won't have punctuation marks

    :param test_string:
    :return:
    """
    # Pre-process the given string. i.e. strip off spaces and convert all to lowercase letters

    test_string = test_string.replace(" ", "")
    test_string = test_string.lower()

    # Fill in dictionary with keys being chars and values being num of occurences
    palindrome_dict = {}

    for item in test_string:

        if item not in palindrome_dict.keys():
            palindrome_dict[item] = 1
        else:
            palindrome_dict[item] += 1

    # Now parse the dictionary and give the decision whether it is Palindrome Permutation or not
    counter = 0
    for key, value in palindrome_dict.items():

        if counter > 1:
            # Early exit
            return False

        if value % 2 != 0:
            counter += 1

    if counter > 1:
        return False
    else:
        return True


class TestClass(unittest.TestCase):
    test_data_list_true = [
        "Abc Ba",
        "Tact Coa",
        "Madam",
        "Bob",
        "Was it a cat I saw",
        "Eva can I see bees in a cave",
        "No lemon ON lemon"

    ]

    test_data_list_false = [
        "ABCABFKJLM"
    ]

    def test_method(self):
        for test_data in self.test_data_list_true:
            self.assertTrue(is_palindrome_permutation(test_data))

    def test_method_2(self):
        for test_data in self.test_data_list_false:
            self.assertFalse(is_palindrome_permutation(test_data))


if __name__ == "__main__":
    unittest.main()

