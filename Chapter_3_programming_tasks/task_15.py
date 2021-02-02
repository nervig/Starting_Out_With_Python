number_of_seconds = int(input("Enter a number of seconds: "))
if 60 <= number_of_seconds < 3600:
    minutes = number_of_seconds // 60
    seconds = number_of_seconds % 60
    print("{}:{}".format(minutes, seconds))
elif 3600 <= number_of_seconds < 86400:
    # get hours
    hours = number_of_seconds // 3600
    # get remaining time without hours
    remaining_minutes = number_of_seconds % 3600
    # get minutes
    minutes = remaining_minutes // 60
    # get seconds
    seconds = remaining_minutes % 60
    print("{}:{}:{}".format(hours, minutes, seconds))
elif number_of_seconds >= 86400:
    # get days
    days = number_of_seconds // 86400
    # get remaining time without days
    remaining_hours = number_of_seconds % 86400
    # get hours
    hours = remaining_hours // 3600
    # get remaining time without hours
    remaining_minutes = remaining_hours % 3600
    # get minutes
    minutes = remaining_minutes // 60
    # get seconds
    seconds = remaining_minutes % 60
    print("{}d:{}h:{}m:{}s".format(days, hours, minutes, seconds))