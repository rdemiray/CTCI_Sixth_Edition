def binary_to_decimal(binary):
    """
    Binary to decimal converter using loop

    :param binary: [String] "0101010101"
    :return: [int]
    """
    i = 0
    integer = 0

    size = len(binary)
    while i < len(binary):
        integer += int(binary[size - 1 - i]) * pow(2, i)
        i += 1
    print(integer)


print(binary_to_decimal("00000111"))
