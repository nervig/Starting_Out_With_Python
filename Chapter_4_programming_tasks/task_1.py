amount_bugs = 0
for i in range(1, 6):
    bugs_of_every_day = int(input("How many bugs in {} day?: ".format(i)))
    amount_bugs += bugs_of_every_day
print("Number of bugs for 5 day equals {}".format(amount_bugs))