import random

def squad():
    print('Chosen Squad: ')

    random_num = random.randrange(1, 10)
    
    if random_num == 1:
        print('Alpha')
    elif random_num == 2:
        print('Beta')
    elif random_num == 3:
        print('Charlie')
    elif random_num == 4:
        print('Delta')
    elif random_num == 5:
        print('Echo')
    elif random_num == 6:
        print('Falcon')
    elif random_num == 7:
        print('Gamma')
    elif random_num == 8:
        print('Helio')
    elif random_num == 9:
        print('India')
    elif random_num == 10:
        print('Zeta')
    
    print('Good luck! Stay frosty!')
squad()