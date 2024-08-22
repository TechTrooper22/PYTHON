
'''
 ______
/ [] []\__
|()____()_|

'''

# class Car:
#     color = "Red"
#     brand = "TATA" 
#     average = "200 km/hr"

# car1 = Car()
# print(car1.color)

'''
class Student:
    def __init__(self, name, marks):    # we can write anuthing instead of 'self', but it willl be a practice.
        print("Adding new Student in Database...")
        self.name = name
        self.mark = marks

s1 = Student("karan", 98)
print(s1.name, s1.mark)
s2 = Student("arjun", 89)
print(s2.name, s2.mark) 
'''

'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def getAvg(self):
        avg = 0
        for val in self.marks:
            avg += (val/3)
        return avg
        
s1 = Student("Tejas", [89,95,94])
print("Average marks of",s1.name,"is", s1.getAvg())
'''

'''
class Car:
    # color = "Red"
    # brand = "TATA" 
    # average = "200 km/hr"
    # def getInfo(self):
    #     print(self.color)
    #     print(self.brand)
    #     print(self.average)

    @staticmethod   # by using this line we can avoid the use of 'self'
    def getInfo():
        color = "Red"
        brand = "TATA" 
        average = "200 km/hr"
        print(color)
        print(brand)
        print(average)

car1 = Car()
car1.getInfo()
'''


# Abstraction - Hiding the implementation details of a class and only showing the essential features to user.
# Encapsulation - Wrapping data and functions into a single unit.

'''
# Create Account class with 2 attributes - balance and account no. Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.accountNo = acc

    def debit(self, amt):
        self.amount = amt
        self.balance -= self.amount
        print("Rs",self.amount,"has been debited from your account")
        print("Current balance is",self.balance)

    def credit(self, amt):
        self.amount = amt
        self.balance += self.amount
        print("Rs",self.amount,"has been credited to your account")
        print("Current balance is",self.balance)

    def getBalance(self):
        print("Available balance is",self.balance)

acc1 = Account(10000, 506519443267)
print(acc1.balance)
print(acc1.accountNo)

print(acc1.debit(500))

print(acc1.credit(1500))

print(acc1.getBalance())
'''

'''
# del keyword - used to delete object property or object itself
class Car:
    color = "Red"
    brand = "TATA" 
    average = "200 km/hr"
    symbol = "$"

car1 = Car()
print(car1.color, car1.brand, car1.average, car1.symbol)
del car1.symbol
print(car1.symbol)
'''

'''
# if we want to make an element private, wee used '__'

# class Account:
#     __name = "anonymous"
#     def __init__(self, accNo, accPass):
#         self.accNumber = accNo
#         self.__accPassword = accPass

#     def resetPassword(self):    # can access inside the class only.
#         print("New password is",self.__accPassword)

# acc = Account(506519443267, "Tejas@220203")
# print(acc.accNumber)
# print(acc.__accPassword)
# print(acc.__name)

# acc.resetPassword()


# class Person:
#     __name = "anonymous"
#     def __hello(self):
#         print("Hello Person")

#     def welcome(self):  # only internal function of class can access the private functions or objects.
#         self.__hello()

# p = Person()
# # print(p.__hello())    # will return an error, so first we will comment it out and try to access as written in the line below. 
# print(p.welcome())
'''
 
'''
# Single Inheritance

# class Car:
#     color =  "Black"
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.color)


# Multi Level Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.name = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diesel")
# car1.start()   


# Multiple Inheritance

# class A:
#     varA = "Welcome to class A"
# class B:
#     varB = "Welcome to class B"
# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)
'''

'''
# super()

class Car:
     def __init__(self, type):
         self.type = type

     @staticmethod
     def start():
         print("Car started...")

     @staticmethod
     def stop():
         print("Car stopped...")

class ToyotaCar(Car):
     def __init__(self, name, type):
         self.name = name
         super().__init__(type)  # This symtax helps us to access the parent element. We are saving our data in parent instead of child
      #  self.type = type    # This syntax is used to store the data within child not in parent
         super().start()

car1 = ToyotaCar("Fortuner", "Diesel")
print(car1.type)
car1.start()
'''

'''
# @classmethod
# The @classmethod decorator is a built-in function decorator which is an expression that gets evaluated after your function is defined. The result of that evaluation shadows your function definition. A class method receives the class as the implicit first argument, just like an instance method receives the instance.

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):  # Here 'cls' is a keyword
        cls.name = name    # Person.name = name

p1 = Person()
p1.changeName("Tejas Shrikhande")
print(p1.name)
print(Person.name)
'''

'''

1) Instance method --> (self)
2) Class method --> (cls)
3) Static method --> ()

# Class Method vs Static Method

A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in Python to create a class method and we use @staticmethod decorator to create a static method in Python.
'''

'''
# @property
# If we don't use @property --> if we change any value of phy, chem, math, the value of percentage won't change.
# If we do use @property --> if we change any value of phy, chem, math, the value of percentage will also change.
# Returns the latest value

class Student:
    def __init__(self, phy, chem, math):
        self.physics = phy
        self.chemistry = chem
        self.mathematics = math

    @property
    def calPercentage(self):
        return str((self.physics + self.chemistry + self.mathematics) / 3) + "%"

s1 = Student(88,96,93)
print(s1.calPercentage)

s1.physics = 99
print(s1.calPercentage)
'''

'''
# Dunder Function
    # a+b --> a.__add__(b)
    # a-b --> a.__sub__(b)
    # a*b --> a.__mul__(b)
    # a/b --> a.__truediv__(b)
    # a%b --> a.__mod__(b)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(3, 1)
num2.showNumber()

num3 = num1 + num2  # num3 = num1,__add__(num2) 
num3.showNumber()

num4 = num1 - num2  # num3 = num1,__sub__(num2)
num4.showNumber()
'''

'''
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Dept:", self.dept)
        print("Salary:", self.salary)    

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name:", self.name)
        print("Age:", self.age)
        super().__init__("Engineer", "IT", "1,00,000")

eng1 = Engineer("Tejas Shrikhande", 40)
eng1.showDetails()
'''

'''
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price
    
o1 = Order("Chips", 20)
o2 = Order("tea", 13)

print(o1.__gt__(o2)) # True
print(o1 > o2) # True
'''