ocean_level = 0
print("Year\t\tLevel+\n"
      "-----------------")
for i in range(1, 25 + 1):
    ocean_level += 1.6
    print("{}\t\t\t{}".format(i, round(ocean_level, 1)))