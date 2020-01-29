import unittest
from collections import Counter


def check_permutation_1(string1, string2):
    """
    Use Python's built in structure => Counter
    """

    if len(string1) != len(string2):
        return False

    my_counter = Counter()
    for character in string1:
        my_counter[character] += 1

    for character in string2:
        if my_counter[character] == 0:
            return False
        my_counter[character] -= 1
    return True


def check_permutation_2(string1, string2):
    """
    Do not use Counter, use dictionary instead
    """
    # First, check whether string lengths are equal (EARLY EXIT)
    if len(string1) != len(string2):
        return False
    # Key: [string], Value: [Int] E.g. {"a":5, "b": 10, "c":4}
    char_dictionary = {}

    for item in string1:
        # Increment if key already exists, add to dictionary first and then increment otherwise

        if item not in char_dictionary.keys():
            char_dictionary[item] = 1
        else:
            char_dictionary[item] += 1

    # Now we've collected all chars in the dictionary

    # Iterate over second string and decrement values each time
    for item in string2:

        if item in char_dictionary.keys():
            if char_dictionary[item] == 0:
                return False

            char_dictionary[item] -= 1
        else:
            # A character in the second string is not even in the dictionary
            return False

    return True


class Test(unittest.TestCase):
    test_data_list_true = [
        ("abcd", "dcba"),
        ("aaabccdddd", "dcbadddcaa"),
    ]

    test_data_list_false = [
        ("Muharrem", "Asya"),
        ("abcd", "dcbaa"),
    ]

    def test_method(self):

        for item in self.test_data_list_true:
            self.assertTrue(check_permutation_1(item[0], item[1]))

        for item in self.test_data_list_false:
            self.assertFalse(check_permutation_1(item[0], item[1]))

    def test_method_2(self):
        for item in self.test_data_list_true:
            self.assertTrue(check_permutation_2(item[0], item[1]))

        for item in self.test_data_list_false:
            self.assertFalse(check_permutation_2(item[0], item[1]))


if __name__ == "__main__":
    unittest.main()
