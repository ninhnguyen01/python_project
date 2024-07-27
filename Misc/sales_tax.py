# Sales Tax program
state_sales_tax = 0.05
county_sales_tax = 0.025
total_sales_tax = state_sales_tax + county_sales_tax 

purchase = float(input('Enter the amount of purchase: '))
purchase_sales_tax = purchase * total_sales_tax
total_of_sale = purchase + purchase_sales_tax
print(total_of_sale)