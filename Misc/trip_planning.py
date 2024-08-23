budget = 1500
gas = 600
food = 300
hotel = 200
souvenir = 25
number_of_souvenir = ((budget - gas - food - hotel) // souvenir)
print(number_of_souvenir)