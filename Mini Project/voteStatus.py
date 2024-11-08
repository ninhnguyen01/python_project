''' To register to vote in California, you must be:
        A United States citizen and a resident of California,
        18 years old or older on Election Day,
        Not currently serving a state or federal prison term for the conviction of a felony,
        Not currently found mentally incompetent to vote by a court. '''

# User input
status = input("Enter 'YES' if you are A United States citizen and a resident of California. Otherwise 'NO': ")
age = input("Enter 'YES' if 18 years old or older on Election Day. Otherwise 'NO': ")
prison_term = input("Enter 'NO if not currently serving a state or federal prison term for the conviction of a felony. Otherwise 'YES': ")
mental_status = input("Enter 'NO' if not currently found mentally incompetent to vote by a court. Otherwise 'YES': ")

# Condition
if status.upper() == 'YES' and age.upper() == 'YES' and prison_term.upper() == 'NO' and mental_status.upper() == 'NO':
    print('You are ELIGIBLE to vote in a Primary or General Election!')
else:
    print('You are NOT ELIGIBLE to vote in a Primary or General Election!')