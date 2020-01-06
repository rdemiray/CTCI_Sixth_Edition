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
    pass









class Test(unittest.TestCase):
    test_data_list_true = [
        ("abcd", "dcba"),
    ]

    test_data_list_false = [
        ("Muharrem", "Asya"),
    ]



    def test_method(self):

        for item in self.test_data_list_true:
            self.assertTrue(check_permutation_1(item[0], item[1]))

        for item in self.test_data_list_false:
            self.assertFalse(check_permutation_1(item[0], item[1]))





if __name__ == "__main__":
    unittest.main()