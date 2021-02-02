def main():
    sales_week = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    total_sales = 0
    for day in sales_week:
        sales_week[day] = int(input('Enter sales in ' + day + ' :'))
        total_sales += sales_week[day]
    print('Weekly sales were ' + str(total_sales))


main()