def day_of_week(day):
    match day:
        case 2:
            return "Today is Monday"
        case 3:
            return "Today is Tuesay"
        case 4:
            return "Today is Wedensday"
        case 5:
            return "Today is Thursday"
        case 6:
            return "Today is Friday"
        case 7:
            return "Today is Saturday"
        case 1:
            return "Today is Sunday"
        case _:
            return "Invalid day"
print()        
day_number = int(input("Enter the day number: "))
print(day_of_week(day_number))
print()