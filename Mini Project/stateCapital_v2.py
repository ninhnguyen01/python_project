# Import package
import pandas as pd

# Dictionary database of U.S. States and their capital
state_capital = {'Alabama' : 'Montgomery',
                 'Alaska' : 'Juneau',
                 'Arizona' : 'Phoenix',
                 'Arkansas' : 'Little Rock',
                 'California' : 'Sacramento',
                 'Colorado' : 'Denver',
                 'Connecticut' : 'Hartford',
                 'Delaware' : 'Dover',
                 'Florida' : 'Tallahassee',
                 'Georgia' : 'Atlanta',
                 'Hawaii' : 'Honolulu',
                 'Idaho' : 'Boise',
                 'Illinois' : 'Springfield',
                 'Indiana' : 'Indianapolis',
                 'Iowa' : 'Des Moines',
                 'Kansas' : 'Topeka',
                 'Kentucky' : 'Frankfort',
                 'Louisiana' : 	'Baton Rouge',
                 'Maine' : 'Augusta',
                 'Maryland' : 'Annapolis', 	
                 'Massachusetts' : 'Boston',
                 'Michigan' : 'Lansing',
                 'Minnesota' : 'Saint Paul',
                 'Mississippi' : 'Jackson',
                 'Missouri' : 'Jefferson City',
                 'Montana' : 'Helena',
                 'Nebraska' : 'Lincoln',
                 'Nevada' : 'Carson City',
                 'New Hampshire' : 'Concord',
                 'New Jersey' : 'Trenton',
                 'New Mexico' : 'Santa Fe',
                 'New York' : 'Albany',
                 'North Carolina' : 'Raleigh',
                 'North Dakota' : 'Bismarck',
                 'Ohio' : 'Columbus',
                 'Oklahoma' : 'Oklahoma City',
                 'Oregon' : 'Salem',
                 'Pennsylvania' : 'Harrisburg',
                 'Rhode Island' : 'Providence',
                 'South Carolina' : 'Columbia',
                 'South Dakota' : 'Pierre',
                 'Tennessee' : 'Nashville',
                 'Texas' : 'Austin',
                 'Utah' : 'Salt Lake City',
                 'Vermont' : 'Montpelie',
                 'Virginia' : 'Richmond',
                 'Washington' : 'Olympia',
                 'West Virginia' : 'Charleston',
                 'Wisconsin' : 'Madison',
                 'Wyoming' : 'Cheyenne'}	

# Function to look up your state
def search_state():
    search = input('Enter the name of your state: ').title()
    if search in state_capital.keys():
        print('Result...')
        print('State: {} \nState Capital: {}'.format(search, state_capital[search])) # return state and capital
        exit()
    else:
        print('Your state is NOT IN the DATABASE.')
        print('Would you like to try a new search?')
        re_entry = input("Enter 'Y' for yes. Otherwise, 'N' for no: ")
        while re_entry.upper() == 'Y':
            search_state()
        # print statement for 'N'
        print('Exiting search...')    

# Function to export data to Excel
def export():
    export_data = input("Enter 'Y' to export data to Excel. Otherwise 'N to cancel: ")
    if export_data.upper() == 'Y':
        df = pd.DataFrame(list(state_capital.items()), columns=['State', 'Capital'])
        df.to_excel('database.xlsx', index=False)
        print('Export completed...')
        print('Please check your file folder...')
    else:
        print('Export canceled...')
        exit()

# Function to call search_state() or export()
user_input = input("Enter '1' to Search Database,\nEnter '2' to Export Data,\nEnter '3' to exit: ")
if user_input == '1':
    search_state()
elif user_input == '2':
    export()
else:
    print('Exiting...')
    exit()