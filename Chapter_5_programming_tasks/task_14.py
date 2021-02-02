# distance = 1/2 * g * t**2, where g is 9.8
def falling_distance(time_sec):
    distance = 1 / 2 * 9.8 * time_sec ** 2
    return distance


def main():
    for i in range(1, 11):
        distance_in_meters = falling_distance(i)
        print(round(distance_in_meters))


main()