class User:
    def __init__(self, username):
        self.username = username

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Seller(User):
    def __init__(self, username):
        super().__init__(username)
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class Customer(User):
    def __init__(self, username):
        super().__init__(username)
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def calculate_total(self):
        total = 0
        for product in self.cart:
            total += product.price
        return total

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

class Payment:
    @staticmethod
    def checkout(order):
        total = order.customer.calculate_total()
        print(f"Total amount to be paid: ${total}")
        decision = input("Do you want to buy these products? (yes/no): ").lower()
        if decision == "yes":
            print("Thank you for buying!")
        else:
            print("Thank you for visiting!")
#usage
seller1 = Seller("Seller1")
seller1.add_product(Product("Product1", 10))
seller1.add_product(Product("Product2", 20))

customer = Customer("Customer1")
customer.add_to_cart(seller1.products[0])
customer.add_to_cart(seller1.products[1])

order = Order(customer, customer.cart)
Payment.checkout(order)
