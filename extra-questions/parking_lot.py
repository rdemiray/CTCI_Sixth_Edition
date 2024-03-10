
def get_cost(hours):
    """
    Returns hourly cost of parking lot based in the hours stayed in the parking lot
    :param hours:
    :return:
    """
    if 0 < hours < 3:
        return 15

    if 2 < hours < 7:
        return 25.5

    if 6 < hours < 11:
        return 30

    if hours > 10:
        return 37.7


money_earned = 0.0

while True:
    print("Please enter the vehicle code...E.g. 1, 2, 3, 4")
    vehicle_code = int(input())
    if vehicle_code == 0:
        break

    print("Now enter how many hours you have stayed in the parking lot ")
    num_of_hours = int(input())
    cost = 0

    if vehicle_code == 1:
        # Motorcycle
        cost = 0.5 * get_cost(num_of_hours)
    elif vehicle_code == 2:
        # Automobile
        cost = 1.0 * get_cost(num_of_hours)
    elif vehicle_code == 3:
        # Minibus
        cost = 1.5 * get_cost(num_of_hours)
    elif vehicle_code == 4:
        # Bus
        cost = 2.0 * get_cost(num_of_hours)

    money_earned = money_earned + cost

print("Total money made is {} TL".format(money_earned))


