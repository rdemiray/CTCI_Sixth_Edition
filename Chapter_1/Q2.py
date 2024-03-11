import unittest
from collections import Counter


def check_permutation_1(string1, string2):
    """
    Use Python's built-in structure => Counter
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


def check_permutation_3(string1, string2):
    """

    :param string1:
    :param string2:
    :return:
    """

    if len(string1) != len(string2):
        return False
    global_dict = {}
    for char in string1:
        if global_dict.get(char) is None:
            global_dict[char] = 1
        else:
            global_dict[char] += 1

    for char in string2:
        if global_dict[char] == 0:
            return False
        global_dict[char] -= 1

    return True


def are_permutations(str1, str2):
    """
    ChatGPT generated code

    :param str1:
    :param str2:
    :return:
    """
    # If the lengths of the strings are different, they can't be permutations
    if len(str1) != len(str2):
        return False

    # Convert strings to lists for easy manipulation
    str1_list = list(str1)
    str2_list = list(str2)

    # Sort the lists
    str1_list.sort()
    str2_list.sort()

    # Compare the sorted lists
    if str1_list == str2_list:
        return True
    else:
        return False


class Test(unittest.TestCase):
    test_data_list_true = [
        ("abcd", "dcba"),
        ("aaabccdddd", "dcbadddcaa"),
        ("silent", "listen")
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

    def test_method_3(self):
        for item in self.test_data_list_true:
            self.assertTrue(are_permutations(item[0], item[1]))

        for item in self.test_data_list_false:
            self.assertFalse(are_permutations(item[0], item[1]))

    def test_method_4(self):
        for item in self.test_data_list_true:
            self.assertTrue(check_permutation_3(item[0], item[1]))

        for item in self.test_data_list_false:
            self.assertFalse(check_permutation_3(item[0], item[1]))


if __name__ == "__main__":
    unittest.main()
