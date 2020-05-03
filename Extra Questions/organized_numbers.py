def is_organized_number(number):
    """
    Checks if the given number is organized number
    40585 = 4! + 0! + 5! + 8! + 5!
    145 = 1! + 4! + 5!

    :param number:
    :return:
    """

    string_form = str(number)
    sum = 0

    for num in string_form:
        sum += factorial(int(num))

    if sum == number:
        # Organized number
        return True
    else:
        # Not organized number
        return False


def factorial(number):
    """

    :param number:
    :return:
    """
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


def find_all_organized_numbers(number):
    """

    :param number:
    :return:
    """

    list_of_all_organized_numbers = []

    for i in range(number):
        if is_organized_number(i):
            list_of_all_organized_numbers.append(i)

    # Print all organized numbers to the console

    for item in list_of_all_organized_numbers:
        print("{} is an organized number \n".format(item))



find_all_organized_numbers(40586)



