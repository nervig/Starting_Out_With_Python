def main():
    rainfall_mounths = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'Jule': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}
    total_rainfall = 0
    max_rainfall = 0
    min_rainfall = 500
    for mounth in rainfall_mounths:
        rainfall_mounths[mounth] = int(input('Enter a rainfall per ' + mounth + ': '))
        total_rainfall += rainfall_mounths[mounth]
        if rainfall_mounths[mounth] > max_rainfall:
            max_rainfall = rainfall_mounths[mounth]
        elif rainfall_mounths[mounth] < min_rainfall:
            min_rainfall = rainfall_mounths[mounth]

    print('Total amount of rainfall per year: ' + str(total_rainfall))
    print('Average rainfall per month: ' + str(total_rainfall / 12))
    print('Maximum amount of rainfall per month: ' + str(max_rainfall))
    print('Minimum amount of rainfall per month: ' + str(min_rainfall))


main()
