number_of_participants = int(input("Enter a number of participants "))
quantity_for_each_participants = int(input("Enter a quantity for each participants "))
# Sausages in packs of 10. Number of packages of sausages = (number_of_participants * quantity_for_each_participants)
# // 10
number_of_sausages = number_of_participants * quantity_for_each_participants
number_of_packages_of_sausages = number_of_sausages // 10
if number_of_sausages % 10 != 0:
    number_of_packages_of_sausages += 1
# Buns packed in 8 pieces. Number of packages of buns = (number_of_participants * quantity_for_each_participants) // 8
number_of_buns = number_of_participants * quantity_for_each_participants
number_of_packages_of_buns = number_of_buns // 8
if number_of_buns % 8 != 0:
    number_of_packages_of_buns += 1
print("Number of packages of sausages " + str(number_of_packages_of_sausages))
print("Number of packages of buns " + str(number_of_packages_of_buns))
print("Number of sausages remaining " + str(number_of_packages_of_sausages * 10 - number_of_sausages))
print("Number of buns remaining " + str(number_of_packages_of_buns * 8 - number_of_buns))
