class Item:
    pay_rate = 0.8 # Pay rate after 20% DISCOUNT
    all = []
    
    def __init__(self, name: str, price: float, quantity):
        # Run validation
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign to object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_DISCOUNT(self, price):
        self.price = price * self.pay_rate

item1 = Item("PHONE", 100, 5)
item2 = Item("LAPTOP", 1000, 3)
item3 = Item("CABLE", 10, 5)
item4 = Item("MOUSE", 50, 5)
item5 = Item("KEYBOARD", 75, 5)

print([instance.name for instance in Item.all])
print("\n")

# Item 1
print(f"The {item1.name} is PRICED at {item1.price} with {item1.quantity} quantity left")
print(f"The TOTAL VALUE is {item1.calculate_total_price()}")
print('\n')
item1.apply_DISCOUNT(item1.price)
print(f"The price for 1 item with DISCOUNT is {item1.price}")
print('\n')

# Item 2
print(f"The {item2.name} is PRICED at {item2.price} with {item2.quantity} quantity left")
print(f"The TOTAL VALUE is {item2.calculate_total_price()}")
print('\n')
item2.pay_rate = 0.7
item2.apply_DISCOUNT(item2.price)
print(f"The price for 1 item with DISCOUNT is {item2.price}")
print('\n')

# Item 3
print(f"The {item3.name} is PRICED at {item3.price} with {item3.quantity} quantity left")
print(f"The TOTAL VALUE is {item3.calculate_total_price()}")
print('\n')
item3.apply_DISCOUNT(item3.price)
print(f"The price for 1 item with DISCOUNT is {item3.price}")
print('\n')

# Item 4
print(f"The {item4.name} is PRICED at {item4.price} with {item4.quantity} quantity left")
print(f"The TOTAL VALUE is {item4.calculate_total_price()}")
print('\n')
item4.apply_DISCOUNT(item4.price)
print(f"The price for 1 item with DISCOUNT is {item4.price}")
print('\n')

# Item 5
print(f"The {item5.name} is PRICED at {item5.price} with {item5.quantity} quantity left")
print(f"The TOTAL VALUE is {item5.calculate_total_price()}")
print('\n')
item5.apply_DISCOUNT(item5.price)
print(f"The price for 1 item with DISCOUNT is {item5.price}")
print('\n')