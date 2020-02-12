import unittest


def is_one_away(test_string_1, test_string_2):
    """
    E.g.
    pale, ple => True
    pales, pale => True
    pale, bale => True
    pale, bake => False

    :param test_string_1:
    :param test_string_2:
    :return: [bool] True, False
    """

    if len(test_string_1) == len(test_string_2):
        # Equal length case
        return one_away_equal_size(test_string_1, test_string_2)
    elif len(test_string_1) + 1 == len(test_string_2):
        # Insertion Case
        return one_away_diff_size(test_string_1, test_string_2)
    elif len(test_string_1) == len(test_string_2) + 1:
        # Deletion case
        return one_away_diff_size(test_string_2, test_string_1)
    else:
        print("Given strings are more than 1 difference away from each other")
        return False


def one_away_equal_size(string1, string2):
    """

    :param string1:
    :param string2:
    :return:
    """
    num_of_difference = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            num_of_difference += 1

            if num_of_difference > 1:
                return False

    return True


def one_away_diff_size(string1, string2):
    """
    string2 will always be longer than string1....

    :param string1:
    :param string2:
    :return:
    """

    index_1 = 0
    index_2 = 0

    num_of_difference = 0

    for i in range(len(string2)):

        if string1[index_1] == string2[index_2]:
            # keep moving
            index_1 += 1
            index_2 += 1
        else:
            # Only increment index_2 (index of the longer string)
            index_2 += 1
            num_of_difference += 1

            if num_of_difference > 1:
                return False

    return True


class TestClass(unittest.TestCase):
    test_data_true = [("Asya", "Aska"),
                      ("Asya", "Asa"),
                      ("Asya", "Askya"),
                      ]
    test_data_false = [("Book", "BookBook"),
                       ("Book", "Buuk"),
                       ("Book", "Bk"),
                       ("Book", "Bmmk"),
                       ]

    def test_method_true(self):
        for item in self.test_data_true:
            self.assertTrue(is_one_away(item[0], item[1]))

    def test_method_false(self):
        for item in self.test_data_false:
            self.assertFalse(is_one_away(item[0], item[1]))


if __name__ == "__main__":
    unittest.main()



