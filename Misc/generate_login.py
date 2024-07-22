# system login

# import package
import login 

# main function
def main():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')
    print('Your system login name is:')
    print(login.get_login_name(first,last,idnumber))

# call main function
if __name__ == '__main__':
    main()