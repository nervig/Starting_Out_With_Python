print("Celsius\t\tFahrenheit")
print("----------------------")
# for i in range(1, 21):
#     fahrenheit = (9 / 5) * i + 32
#     print("{}\t\t\t{}".format(i, round(fahrenheit)))

i = 1
while 0 < i < 21:
    fahrenheit = (9 / 5) * i + 32
    print("{}\t\t\t{}".format(i, round(fahrenheit)))
    i += 1