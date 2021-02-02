def main():
    distance = float(input("Enter a distance in kilometer: "))
    distance_in_mile = kilometer_to_mile(distance)
    print("The distance in miles equals %f" % float(format(distance_in_mile, '.2f')))


def kilometer_to_mile(number):
    return number * 0.6214


main()