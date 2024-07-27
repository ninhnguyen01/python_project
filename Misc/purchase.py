# Single Purchase program
item_price = float(input('Enter the price for an item: '))
sub_total = item_price
sales_tax = 0.07
sub_total += sub_total * sales_tax
print(sub_total)