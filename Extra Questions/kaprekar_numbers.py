
def is_kaprekar_number(num):
    """
    Returns true if n is a Kaprekar number, else false

    A Kaprekar number is a number whose square when divided into two parts and such that sum of parts is equal
    to the original number and none of the parts has value 0

    :param num:
    :return:
    """
    string_num = str(num**2)
    left_string = string_num[:len(string_num)//2]
    right_string = string_num[len(string_num)//2:]
    left_num = int(left_string) if left_string != '' else 0
    right_num = int(right_string) if right_string != '' else 0
    if num == left_num + right_num:
        return True
    return False


print(is_kaprekar_number(55))
