class User:
    def __init__(self, username):
        self.username = username

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Seller(User):
#call the parent class using super()
#add products 

class Customer (User):
#call the parent class using super()
#add to cart
#calculate the total

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

class Payment:
#checkout print the total amount and ask for input if the user wants to buy the products add a yes/no question
  
