speed_vehicle = int(input("Enter a speed of vehicle: "))
travel_time = int(input("Enter a travel time: "))
print("Hour\tDistance traveled")
print("-------------------------")
for i in range(1, travel_time + 1):
    distance_each_hour = i * speed_vehicle
    print("{}\t\t{}".format(i, distance_each_hour))