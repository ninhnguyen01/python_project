class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        balance = sum(item['amount'] for item in self.ledger)
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description:<23}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    total_spent = 0
    category_spent = {}

    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spent[category.name] = spent
        total_spent += spent

    percentages = {name: (spent / total_spent) * 100 if total_spent > 0 else 0
                   for name, spent in category_spent.items()}

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages.values():
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    ----------\n"
    max_length = max(len(name) for name in percentages.keys())
    for i in range(max_length):
        chart += "     "
        for name in percentages.keys():
            chart += name[i] + "  " if i < len(name) else "   "
        chart += "\n"

    return chart.rstrip("\n")  