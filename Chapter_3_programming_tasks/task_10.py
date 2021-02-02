# code with if-else construction:
# coins = 0
# if coins < 101:
#     coins = int(input("Enter coin denomination(5, 10 or 50): "))
#     coins += int(input("Enter coin denomination(5, 10 or 50): "))
#     if coins == 100:
#         print("Congratulations! You win!")
#     elif coins < 101:
#         coins += int(input("Enter coin denomination(5, 10 or 50): "))
#         if coins > 100:
#             print("You lose")
#         elif coins < 101:
#             coins += int(input("Enter coin denomination(5, 10 or 50): "))
#             if coins == 100:
#                 print("Congratulations! You win!")
#             elif coins < 101:
#                 coins += int(input("Enter coin denomination(5, 10 or 50): "))
#                 if coins > 100:
#                     print("You lose")
#                 elif coins < 101:
#                     coins += int(input("Enter coin denomination(5, 10 or 50): "))
#                     if coins == 100:
#                         print("Congratulations! You win!")
#                     elif coins < 101:
#                         coins += int(input("Enter coin denomination(5, 10 or 50): "))
#                         if coins > 100:
#                             print("You lose")
#                         elif coins < 101:
#                             coins += int(input("Enter coin denomination(5, 10 or 50): "))
#                             if coins == 100:
#                                 print("Congratulations! You win!")
#                             elif coins < 101:
#                                 coins += int(input("Enter coin denomination(5, 10 or 50): "))
#                                 if coins > 100:
#                                     print("You lose")
#                                 elif coins < 101:
#                                     coins += int(input("Enter coin denomination(5, 10 or 50): "))
#                                     if coins == 100:
#                                         print("Congratulations! You win!")
#                                     elif coins > 100:
#                                         print("You lose")
coins = 0
while coins < 100:
    input_coins = int(input("Enter coin denomination(5, 10 or 50): "))
    if input_coins == 5 or input_coins == 10 or input_coins == 50:
        coins += input_coins
        if coins == 100:
            print("Congratulations! You win!")
            break
        elif coins > 100:
            print("You lose")
            break
    else:
        print("Error. Enter valid data!")

