# weight in H = weight in kg * 9.8
user_weight_in_kg = float(input("Enter your weight in kg: "))
user_weight_in_H = user_weight_in_kg * 9.8
print(round(user_weight_in_H))
if user_weight_in_H > 500:
    print("Your body is too heavy!")
if user_weight_in_H < 100:
    print("Your body is too light!")
