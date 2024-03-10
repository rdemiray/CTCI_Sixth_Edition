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


def find_max_consecutive_ones(given_string: str) -> int:
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


def find_max_consecutive_ones_2(given_string: str) -> int:
    """

    :param given_string:
    :return:
    """
    # Handle edge case at the beginning of the method
    if int(given_string) == 0:
        return 0

    pointer = 0
    counter = 1
    max_consecutive_repetition = 0

    # Iterating from left to right
    for digit in given_string:

        if pointer != len(given_string) - 1:
            current_digit = int(digit)
            next_digit = int(given_string[pointer + 1])

            if current_digit and next_digit:
                counter += 1
            else:
                # Reset counter and check whether counter is bigger than global max
                if counter > max_consecutive_repetition:
                    max_consecutive_repetition = counter
                    counter = 1

            # Increment index at the end of the loop
            pointer += 1
        else:
            if counter > max_consecutive_repetition:
                max_consecutive_repetition = counter

    return max_consecutive_repetition


def find_max_consecutive_ones_3(given_string: str) -> int:
    """
    NOT A GREAT IDEA!

    :param given_string:
    :return:
    """
    counter = 1
    global_max = 0
    for i in range(len(given_string) - 1):

        while int(given_string[i]) and int(given_string[i+1]):
            counter += 1
            i += 1
        # Once we get out of while loop, check local max against global max and reset counter
        if counter > global_max:
            global_max = counter
            counter = 1

    return global_max


"""
Extended Question:
Assume that you can flip one of the zero (0) to one (1)... Write a method which gives the max possible consecutive ones
 if we are to change only one 0 to 1.

E.g. 
"1101100001010000" -> Should return 5. Because if we flip first occurrence of zero to one, then we'll have 5 consecutive 
ones. but if we flip any other zeros, max number we'll end up will be 3.
"""


def max_possible_consecutive_ones(given_string: str) -> int:
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
        current_max = find_max_consecutive_ones(flip_ith_occurrence_of_zero(given_string, i + 1))

        if current_max > global_max:
            global_max = current_max

    return global_max


def flip_ith_occurrence_of_zero(given_string, index):
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

    return string_builder


class TestClass(unittest.TestCase):
    test_data = [
        ("1110001111100001101010101", 5),
        ("0001111", 4),
        ("00000000000000", 0),
        ("111000100", 3),
        ("111111111", 9),
        ("000000100000", 1),
    ]

    test_data_extended = [("1101100001010000", 5)]

    def test_method(self):

        for item in self.test_data:
            self.assertEqual(
                find_max_consecutive_ones(item[0]),
                item[1],
                msg=f"Test failed for the test dataset of: {item}"
            )

    def test_method_2(self):
        for item in self.test_data:
            self.assertEqual(
                find_max_consecutive_ones_2(item[0]),
                item[1],
                msg=f"Test failed for the test dataset of: {item}"
            )

    # def test_method_3(self):
    #     for item in self.test_data:
    #         self.assertEqual(
    #             find_max_consecutive_ones_3(item[0]),
    #             item[1],
    #             msg=f"Test failed for the test dataset of: {item}"
    #         )

    def test_for_extended_question(self):
        for item in self.test_data_extended:
            self.assertEqual(max_possible_consecutive_ones(
                item[0]),
                item[1],
                msg=f"Test failed for the test dataset of: {item}")


if __name__ == "__main__":
    unittest.main()
