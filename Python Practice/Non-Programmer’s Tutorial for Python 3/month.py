current_month = int(input("Which month (1-12): "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']

if 1 <= current_month <= 12:
    print()
    print("Current month:", months[ current_month - 1])
    print()