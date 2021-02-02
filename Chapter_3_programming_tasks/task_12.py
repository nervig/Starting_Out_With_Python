number_packets = int(input("Enter a number of packets: "))
cost_of_packet = 99
total_cost = number_packets * cost_of_packet
discount = 0
if 9 < number_packets < 20:
    discount = 0.1 # 10%
elif 19 < number_packets < 50:
    discount = 0.2 # 20%
elif 49 < number_packets < 100:
    discount = 0.3 # 30%
elif number_packets > 99:
    discount = 0.4 # 40%
total_cost_with_discount = 0
if number_packets > 9:
    total_cost_with_discount = total_cost - (total_cost * discount)
    print("Your discount was: {}".format(total_cost * discount))
    print("Your total cost with discount was: {}".format(total_cost_with_discount))
else:
    print("Your price is: {}".format(total_cost))