import unittest


def urlify(url_string, length):
    """

    :param url_string:
    :param length:
    :return:
    """
    # We will build/reconstruct a new string
    urlifyied_string = ""

    for index in range(length):
        if url_string[index] == " ":
            urlifyied_string = urlifyied_string + "%20"
        else:
            urlifyied_string = urlifyied_string + url_string[index]

    return urlifyied_string


class TestClass(unittest.TestCase):
    test_data_list_true = [
        ("Mr John Smith      ", 13, "Mr%20John%20Smith"),
        ("Mr John Smith      ", 19, "Mr%20John%20Smith%20%20%20%20%20%20"),
    ]

    test_data_list_false = [
        ("Mr John Smith      ", 13, "Mr John Smith"),
    ]

    def test_method_positive_test(self):
        for test_data in self.test_data_list_true:
            self.assertEqual(urlify(test_data[0], test_data[1]), test_data[2])

    def test_method_negative_test(self):
        for test_data in self.test_data_list_false:
            self.assertNotEqual(urlify(test_data[0], test_data[1]), test_data[2])


if __name__ == "__main__":
    unittest.main()
