# Dictionary database for birthday
birthday = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# Locate person or update the database with new person
while True:
    print('REMINDER - Name in database starts with a capital letter!')
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthday:
        print(f'{birthday[name]} is the birthday of {name}')
    else:
        print(f'No birthday information for {name}')
        print('What is their birthday?')
        bday_person = input()
        birthday[name] = bday_person
        print('Birthday database updated!')