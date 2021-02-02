import car

test_car = car.Car()
for i in range(5):
    test_car.accelerate()
    print(test_car.get_speed())

for x in range(5):
    test_car.car_break()
    print(test_car.get_speed())