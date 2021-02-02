increased_tuition_fees = 45000
for i in range(1, 11):
    increased_tuition_fees +=  increased_tuition_fees * 0.03
    print("{}\t\t\t{}".format(i, round(increased_tuition_fees)))
    