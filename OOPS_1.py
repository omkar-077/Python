# 1st ex..

class Car:
    # properties
    name = "Tesla"
    color = "Red"
    fuel = "Electric"

    # methods
    def start(self):
        print("Car is starting...")

    def drive(self):
        print("Car is moving...")

c1 = Car()
print(c1.name)
print(c1.color)
c1.start()
c1.drive()

# 2nd ex..

class BankAccount:
    # properties
    account_holder = "Pratik"
    balance = 50000

    # methods
    def deposit(self):
        print("Money deposited")

    def withdraw(self):
        print("Money withdrawn")

b1 = BankAccount()
print(b1.account_holder)
print(b1.balance)
b1.deposit()
b1.withdraw()


# 3rd ex

class Employee:
    # properties
    emp_id = 101
    name = "Rahul"
    department = "IT"
    salary = 50000

    # methods
    def work(self):
        print("Employee is working...")

    def get_salary(self):
        print("Salary credited")

e1 = Employee()
print(e1.name)
print(e1.department)
e1.work()
e1.get_salary()


# 4th ex..

class Customer:
    # properties
    customer_id = 501
    name = "Amit"
    cart_items = 3

    # methods
    def add_to_cart(self):
        print("Item added to cart")

    def place_order(self):
        print("Order placed successfully")

c1 = Customer()
print(c1.name)
print(c1.cart_items)
c1.add_to_cart()
c1.place_order()


# 5th ex..

class Fan:
    # properties
    brand = "Usha"
    color = "White"
    speed = 3

    # methods
    def on(self):
        print("Fan is ON")

    def off(self):
        print("Fan is OFF")

f1 = Fan()
print(f1.brand)
print(f1.speed)
f1.on()
f1.off()
