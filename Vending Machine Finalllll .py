class VendingMachine:
    def __init__(self):
        # Initialize the vending machine with items, their prices, and initial stock
        self.items = {
            'A1': {'name': 'Tissue', 'price': 1.50, 'stock': 10},
            'A2': {'name': 'Chips', 'price': 1.00, 'stock': 10},
            'B1': {'name': 'Water', 'price': 1.00, 'stock': 10},
            'B2': {'name': 'Chocolate', 'price': 1.20, 'stock': 10},
            'B3': {'name': 'M&M', 'price': 2.00, 'stock': 10},
            'B4': {'name': 'Candy', 'price': 1.70, 'stock': 10},
            'C1': {'name': 'Potato Chips', 'price': 2.50, 'stock': 10},
            'C2': {'name': 'Snickers Bar', 'price': 2.70, 'stock': 10},
            'C3': {'name': 'Doritos', 'price': 1.20, 'stock': 10},
            'D1': {'name': 'Oreo Cookies', 'price': 1.00, 'stock': 10},
            'D2': {'name': 'Kitkat', 'price': 1.10, 'stock': 10},
            'D3': {'name': 'Pringles', 'price': 1.80, 'stock': 10},
        }
        self.money_inserted = 0  # Initialize the amount of money inserted by the user
        self.total_money_inserted = 0  # Initialize the total amount of money inserted for all items chosen

        # Define a dictionary to store item relationships for suggestions
        self.item_relationships = {
            'A1': ['A2', 'B1'],  # Tissue -> Chips, Water
            'A2': ['A1', 'B1'],  # Chips -> Tissue, Water
            'B1': ['A1', 'A2'],  # Water -> Tissue, Chips
            'B2': ['B3', 'D3'],  # Chocolate -> M&M, Pringles
            'B3': ['B2', 'D3'],  # M&M -> Chocolate, Pringles
            'B4': ['C1', 'C2'],  # Candy -> Potato Chips, Snickers Bar
            'C1': ['B4', 'C2'],  # Potato Chips -> Candy, Snickers Bar
            'C2': ['B4', 'C1'],  # Snickers Bar -> Candy, Potato Chips
            'C3': ['D2', 'D1'],  # Doritos -> Kitkat, Oreo Cookies
            'D1': ['C3', 'D2'],  # Oreo Cookies -> Doritos, Kitkat
            'D2': ['C3', 'D1'],  # Kitkat -> Doritos, Oreo Cookies
            'D3': ['B2', 'B3']   # Pringles -> Chocolate, M&M
        }

    def display_menu(self):
        # Display the menu of available items with their codes, names, prices, and stock levels
        print("=== Vending Machine Menu ===")
        for code, item in self.items.items():
            print(f"{code}: {item['name']} - ${item['price']} (Stock: {item['stock']})")
        print("============================")

    def select_item(self):
        # Prompt the user to enter the code of the item they want to purchase
        # Return the code if it's valid, otherwise ask the user to try again
        code = input("Enter item code: ")
        if code in self.items:
            return code
        else:
            print("Invalid item code. Please try again.")
            return self.select_item()

    def insert_money(self):
        # Prompt the user to insert money and update the amount of money inserted
        try:
            amount = float(input("Insert money: $"))
            if amount >= 0:
                self.money_inserted += amount
                self.total_money_inserted += amount  # Accumulate the total money inserted
            else:
                print("Invalid amount. Please insert a non-negative amount.")
                self.insert_money()
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            self.insert_money()

    def dispense_item(self, code):
        # Dispense the selected item if it's in stock and the user has inserted enough money
        # Update the stock and deduct the price from the user's balance
        item = self.items[code]
        if item['stock'] > 0 and self.money_inserted >= item['price']:
            item['stock'] -= 1
            self.money_inserted -= item['price']
            print(f"{item['name']} dispensed. Enjoy your snack!")
            if self.money_inserted > 0:
                print(f"Change returned: ${self.money_inserted:.2f}")
            self.money_inserted = 0
            self.suggest_purchase(code)  # Suggest a purchase after dispensing the item
        elif item['stock'] == 0:
            print("Sorry, this item is out of stock. Please choose another item.")
        else:
            print("Insufficient funds. Please insert more money or choose a cheaper item.")

    def buy_more(self):
        # Ask the user if they want to purchase more items and return True or False based on their input
        return input("Do you want to purchase more snacks? (yes/no): ").lower() == 'yes'

    def suggest_purchase(self, selected_item):
        # Check if there are suggestions for the selected item
        if selected_item in self.item_relationships:
            suggestions = self.item_relationships[selected_item]
            print(f"If you like {self.items[selected_item]['name']}, you may also like:")
            for suggestion_code in suggestions:
                print(f"- {self.items[suggestion_code]['name']} (${self.items[suggestion_code]['price']:.2f})")
        else:
            print("Sorry, no suggestions available for this item.")

    def create_bill(self, items):
        # Create a bill with the purchased items, their prices, total sum, and total money inserted
        bill = "=== Vending Machine Bill ===\n"
        for item in items:
            bill += f"\t{item['name']:20} ${item['price']:.2f}\n"

        total_sum = sum(item['price'] for item in items)
        bill += f"\n\tTotal Sum: ${total_sum:.2f}\n"
        bill += f"\tTotal Money Paid: ${self.total_money_inserted:.2f}\n"
        bill += f"\tTotal Change: ${self.total_money_inserted - total_sum:.2f}\n"

        return bill

    def run(self):
        # Main function to run the vending machine
        purchased_items = []
        while True:
            self.display_menu()
            selected_item = self.select_item()
            self.insert_money()
            self.dispense_item(selected_item)
            purchased_items.append(self.items[selected_item])

            if not self.buy_more():
                print("Thank you for using the vending machine. Have a great day!")
                break

        # Generate and print the bill
        bill = self.create_bill(purchased_items)
        print(bill)


# Example usage:
if __name__ == "__main__":
    # Create an instance of the VendingMachine class and run the vending machine
    vending_machine = VendingMachine()
    vending_machine.run()