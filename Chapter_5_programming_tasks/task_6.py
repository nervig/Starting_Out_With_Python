def main():
    gram_of_fat = int(input("Enter a gram of fat: "))
    gram_of_carbohydrates = int(input("Enter a amount of carbohydrates in grams: "))
    print("The amount calories from fat is {}\n"
          "The amount calories from carbohydrates is {}".format(calculate_calories_fat(gram_of_fat), calculate_calories_carbohydrates(gram_of_carbohydrates)))


def calculate_calories_fat(num):
    calories_fat = num * 9
    return calories_fat


def calculate_calories_carbohydrates(num):
    calories_carbohydrates = num * 4
    return calories_carbohydrates

main()