def main():
    feet_number = float(input("Enter a number of feet: "))
    number_inches = feet_to_inches(feet_number)
    print("In {} feets are {} inches".format(feet_number, number_inches))


def feet_to_inches(num):
    inches = num * 12
    return inches


main()