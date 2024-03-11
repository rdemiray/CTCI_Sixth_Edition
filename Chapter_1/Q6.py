import unittest


def compress_string(given_string):
    """

    :param given_string:
    :return:
    """

    print("Given String is: {}".format(given_string))

    counter = 1
    compressed_string = ""

    for i in range(len(given_string)):

        if i < len(given_string) - 1:
            if given_string[i] == given_string[i + 1]:
                counter += 1
            else:
                compressed_string += given_string[i] + str(counter)
                counter = 1
    #  When we got out of the loop, we haven't appended the last element... Need to append last element
    compressed_string += given_string[i] + str(counter)

    print("Compressed string is: {}".format(compressed_string))

    if len(compressed_string) < len(given_string):
        return compressed_string
    else:
        return given_string


class TestClass(unittest.TestCase):

    test_data_positive = [("aaaabbbbbcccdddee", "a4b5c3d3e2"),
                          ("aaaabbbbbcccddde", "a4b5c3d3e1"),
                          ("abcdef", "abcdef"),
                          ]

    def test_method(self):
        for item in self.test_data_positive:
            self.assertEqual(compress_string(item[0]), item[1])


if __name__ == "__main__":
    unittest.main()
