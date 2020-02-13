import unittest

"""
Question:

Given a string consisting of binary values ("1110001110011"), find the max number of consecutive 1s
E.g.
Sample Input -> Sample Output
"11001010111" -> 3
"11111111" -> 8
"00000000" -> 0
"""


def find_max_consecutive_ones(given_string):
    """

    :param given_string:
    :return:
    """

    counter = 1
    max_consecutive_repetition = 0

    for i in range(len(given_string)):

        if i+1 < len(given_string):
            if given_string[i] == "1" and given_string[i + 1] == "1":
                counter += 1
            elif given_string[i] == "1" and given_string[i + 1] == "0":
                if counter > max_consecutive_repetition:
                    max_consecutive_repetition = counter
                    counter = 1
            elif given_string[i] == "0" and given_string[i + 1] == "1":
                counter = 1
            elif given_string[i] == "0" and given_string[i + 1] == "0":
                counter = 0
        else:
            if counter > max_consecutive_repetition:
                max_consecutive_repetition = counter

    return max_consecutive_repetition


"""
Extended Question:
Assume that you can flip one zero to onw... Write a method which gives the max possible consecutive ones if we are to
change only one 0 to 1.

E.g. 
"1101100001010000" -> Should return 5. Because if we flip first occurence of zero to one, then we'll have 5 consecutive 
ones. but if we flip any other zeros, max number we'll end up will be 3.
"""


def max_possible_consecutive_ones(given_string):
    """

    :param given_string:
    :return:
    """

    # Count number of zeros in the given string

    counter = 0
    global_max = 0
    for item in given_string:
        if item == "0":
            counter += 1

    for i in range(counter+1):
        current_max = find_max_consecutive_ones(flip_ith_occurence_of_zero(given_string, i+1))

        if current_max > global_max:
            global_max = current_max

    return global_max


def flip_ith_occurence_of_zero(given_string, index):
    """

    :param given_string:
    :param index:
    :return:
    """
    local_index = 0
    string_builder = ""

    for item in given_string:

        if item == "0":
            local_index += 1

        if local_index == index:
            string_builder += "1"
        else:
            string_builder += item

    # print("Given string: {}".format(given_string))
    # print("Given index: {}".format(index))
    # print("Flipped string: {}".format(string_builder))

    return string_builder


class TestClass(unittest.TestCase):
    test_data = [("1110001111100001101010101", 5),
                 ("00000000000000", 0),
                 ("111000000", 3),
                 ("0001111", 4),
                 ("111111111", 9),
                 ]

    test_data_extended = [("1101100001010000", 5)]

    def test_method(self):

        for item in self.test_data:
            self.assertEqual(find_max_consecutive_ones(item[0]), item[1])

    def test_for_extended_question(self):
        for item in self.test_data_extended:
            self.assertEqual(max_possible_consecutive_ones(item[0]), item[1])


if __name__ == "__main__":
    unittest.main()









