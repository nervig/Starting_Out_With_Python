date_from_user = input("Enter a date in that format: dd/mm/yy ")
date_split = date_from_user.split("/")
new_date = ''
for i in range(len(date_split)):
    if i == 1:
        if date_split[i] == "1":
            date_split[i] = 'january'
        elif date_split[i] == "2":
            date_split[i] = 'february'
        elif date_split[i] == "3":
            date_split[i] = 'march'
        elif date_split[i] == "4":
            date_split[i] = 'april'
        elif date_split[i] == "5":
            date_split[i] = 'may'
        elif date_split[i] == "6":
            date_split[i] = 'june'
        elif date_split[i] == "7":
            date_split[i] = 'jule'
        elif date_split[i] == "8":
            date_split[i] = 'august'
        elif date_split[i] == "9":
            date_split[i] = 'september'
        elif date_split[i] == "10":
            date_split[i] = 'october'
        elif date_split[i] == "11":
            date_split[i] = 'november'
        elif date_split[i] == "12":
            date_split[i] = 'december'
    new_date += date_split[i] + " "
print(new_date)