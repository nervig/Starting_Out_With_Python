'''
Index of weight of body = Weight / Hight ** 2
'''

weight_of_body = float(input("Enter a weight of your body in kg: "))
hight = float(input("Enter a hight in meter: "))
index_weigh_body =  weight_of_body / hight ** 2
print(index_weigh_body)
if 18.5 <= index_weigh_body <= 25:
    print("Your weight is optimal")
elif index_weigh_body < 18.5:
    print("Your weight is underweight")
elif index_weigh_body > 25:
    print("Your weight is overweight")