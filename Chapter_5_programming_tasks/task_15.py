# kinetic energy = 1/2 * m * v**2, where are: m is weight of body, v is speed of body in metre/sec
def calculate_kinetic_energy(weight_in_kg, speed_in_metre_sec):
    kinetic_energy = 1 / 2 * weight_in_kg * speed_in_metre_sec**2
    return kinetic_energy


def main():
    weight_in_kg = int(input("Enter a weight of body in kg: "))
    speed = int(input("Enter a speed of body in metre/sec: "))
    kinetic_energy = calculate_kinetic_energy(weight_in_kg, speed)
    print("Kinetic energy is " + str(kinetic_energy))


main()