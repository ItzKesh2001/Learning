# Crete a function which will return the multiplication table of a number stored inside a list. 
# Make sure to pass that number as a parameter to the function

# def table(num):
#     for i in range(1, 11):
#         print(num*i)

# li = [2, 3, 4]

# table(li[0])
# table(li[1])
# table(li[2])

# print("Hello, World!")
# # This is a space built for those who break their heads debugging both code
# # and the hardware that stubbornly runs it.
# # So gather your bits, push your thoughts, and git commit your way into this framework!



# num = 153

# rem = num

# sum = 0

# while rem>0:
#     sum += (rem%10)**3
#     rem //= 10

# print("num:", num)
# print("sum:", sum)

# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



# num = 123324

# length = 0

# while num > 0:
#     length += 1
#     num //= 10

# print("Length: ", length)


# students = {
#     'Kabir' : 55,
#     'Amit' : 39,
#     'Rahul' : 45,
#     'Rachita' : 59 
# }

# results = {}

# for student in students:
#     if students[student] > 40:
#         results[student] = 'Pass'
#     else:
#         results[student] = 'Fail'

# print("Results: ",results)


# def withdraw_amount(balance):

#     withdraw = int(input("Enter the amount to withdraw: "))

#     if withdraw > balance:
#         print("Insufficient balance (Balance: ",balance, ")")
    
#     else:
#         balance -= withdraw
#         print("Withdrawal successful. Updated balance: ", balance)

# balance = 10000
# withdraw_amount(balance)

# li = []

# counter = 2

# for i in range(50):
#     li.append(counter)
#     counter += 2

# print("1. Legnth of the list: ", len(li))

# li2 = []

# for i in range(1,51):
#     li2.append(li[-i])

# print("2. Reversed list: ", li2)

# for i in range(50):
#     if li[i] == 44:
#         li[i] = 100

# print("3. updated list: ", li)

# A = "Python Programming Language"
# B = "Best in the World"

# a = A[10:14]
# b = B[-5:]

# word = a.upper() + b.upper()
# print(word)


# li = [1, 2, 3, 4, 5, 2, 3, 5, 6, 7, 8, 9, 10]

# li2 = set(li)

# li = list(li2)

# li = list(set(li))

# print(li)

# class Calculator:
#     def __init__(self,a,b):
#         self.a = int(input("Enter first number: "))
#         self.b = int(input("Enter second number: "))

#         choice = int(input("Enter your choice (1: Addition, 2: Subtraction, 3: Multiplication, 4: Division): "))

#         if choice == 1:
#             self.Addition(a, b)
#         elif choice == 2:
#             self.Subtraction(a, b)
#         elif choice == 3:
#             self.Multiplication(a, b)
#         elif choice == 4:
#             self.Division(a, b)

#     def Addition(self):
#         print(self.a + self.b)

#     def Subtraction(self):
#         print(self.a - self.b)

#     def Multiplication(self):
#         print(self.a * self.b)

#     def Division(self):
#         print(self.a / self.b)



# ob = Calculator()

# class Car:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand  
    
#     def display(self):
#         print("Model:", self.model)
#         print("Brand:", self.brand)


# class Father:
#     def house(self):
#         print("Father's house")
    
#     def car(self):
#         print("Father's car")

# class Son(Father):
#     def bike(self):
#         print("Son's bike")
    
#     def room(self):
#         print("Son's room")

# class Father(Son):
#     def house(self):
#         print("Father's house")
    
#     def car(self):
#         print("Father's car")


# son = Son()
# son.house()
# son.car()
# son.bike()
# son.room()

# father = Father()
# father.house()
# father.car()


# class Person:
#     def __init__(self):
#         self.name = input("Enter your name: ")

# class Doctor(Person):
#     def display(self):
#         print("Doctor's name: ", self.name)

# class Father(Person):
#     def display(self):
#         print("Father's name: ", self.name)



# doctor = Doctor()
# doctor.display()
# father = Father()
# father.display()

# There's an Organization, which provides features to the users, first create an Admin class where create a function named as Products(), 

# Create another class named as Customer that will be inheriting the Admin class 

# and this class contains function such as make_purchase. 

# Now create one more class named as Prime_Customers 

# and inherit Customer class in this class and here define one function as fast_delivery.

# class Admin:
#     def Products(self):
#         print("Mobile phones, laptops, tablets, accessories")
    
# class Customer(Admin):
#     def make_purchase(self):
#         print("Purchase made successfully")

# class Prime_Customer(Customer):
#     def fast_delivery(self):
#         print("This customer has fast delivery")

# prime_customer = Prime_Customer()
# prime_customer.Products()
# prime_customer.make_purchase()
# prime_customer.fast_delivery()


# from abc import ABC, abstractmethod

# class Notification(ABC):
    
#     @abstractmethod
#     def send_notification(self):
#         pass

# class Email(Notification):
    
#     def send_notification(self):
#         self.email = input("Enter your Email: ")
#         print("Notification sent to ", self.email)

# class WhatsApp(Notification):

#     def send_notification(self):
#         self.phone = input("Enter your WhatsApp number: ")
#         print("Notification sent via WhatsApp to ", self.phone)

# class SMS(Notification):

#     def send_notification(self):
#         self.phone = input("Enter your phone number: ")
#         print("Notification sent via SMS to ", self.phone)

# tup = (10,20,30,40,50)

# print("Sum = ", tup[0] + tup[1] + tup[2] + tup[3] + tup[4])

# class Student:

#     def fun1(self, name):
#         self.name = name
#         return self.name

#     def message(self):
#         print(self.name)
    
# student = Student()
# print(student.fun1("keshav"))
# student.message()

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def __init__(self, brand, model, rate):
#         pass

#     def display(self):
#         pass

#     def return_rate(self):
#         pass

# class Car(Vehicle):

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.rate = 1500

#     def display(self):
#         print("Brand: ", self.brand)
#         print("Model: ", self.model)
#         print("Rate: ", self.rate, "/day")

#     def return_rate(self):
#         return self.rate

# class Bike(Vehicle):

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.rate = 500
    
#     def display(self):
#         print("Brand: ", self.brand)
#         print("Model: ", self.model)
#         print("Rate: ", self.rate, "/day")

#     def return_rate(self):
#         return self.rate
    
# print("Welcome to Vehicle Rentals!")
# print("\nCAR")
# car1 = Car("Honda", "City")
# car1.display()

# print("\nBIKE")
# bike1 = Bike("Yamaha", "R15")
# bike1.display()

# choice = int(input("\n1) Car \n2) Bike \nEnter your choice (1 or 2): "))

# days = int(input("Enter number of days: "))

# insurance = input("Insurance of 200/day? (Y/N): ")

# total = 0

# if choice == 1:
#     total = days * car1.return_rate() 

# elif choice == 2:
#     total = days * bike1.return_rate()

# if insurance == 'Y' or insurance == 'y':
#     total += days * 200

# if days > 7:
    
#     total -= 500

# print("\nYour bill summary\n")
# print("Vehicle:")
# if choice == 1:
#     car1.display()
# elif choice == 2:
#     bike1.display()

# print("Insurance? ", insurance)

# print("Bill total: ", total)


# class Rent_Vehicle:
#     def __init__(self):
#         print('Available Cars:')
#         self.CarDetails()
#         print('Available Bikes: ')
#         self.bikeDetails()


#     def CarDetails(self):
#         self.car_names = ['i20','Innova','Hector','Sonet','Baleno']
#         print('Displaying available cars: ')
#         for x in self.car_names:
#             print("Vehicle Name: ",x)

#         print('Price for every car: 1500 per/day')

#     def bikeDetails(self):
#         self.bike_names = ['MT-15','CB300R','CB350','RE-Hunter','Triumph','Activa']
#         print('Displaying available bikes: ')
#         for x in self.bike_names:
#             print("Vehicle Name: ",x)

#         print('Price for every bike: 500 per/day')

# class Users(Rent_Vehicle):
#     def prices(self):
#         print('Base Bike Price: 500')
#         print('Base Car Price: 1500')

#     def book_vehicle(self):
#         name = input('Enter Vehicle Name: ')
#         for x in self.car_names:
#             if x==name:
#                 inp = int(input('Enter the number of days: '))
#                 print('Calculating your Bill:')
#                 bill = inp*1500
#                 print("Charges: ",bill)
#                 insurance = input('Do you want to go for insurance 200 per/day. Enter True/False: ')
                
#                 if insurance=="True":
#                     insurance_amount = inp*200
#                     print("Final Price: ",bill+insurance_amount)
#                 confirmation = int(input('Enter 1 to confirm: '))
#                 if confirmation==1:
#                     if inp>5:
#                         bill = bill-500

#                     print('Booking Confirmed')
#                     print('Car Name:',name)
#                     print('Amount:',bill)
#                 else:
#                     print('Booking Cancelled')
#                     return

#         for x in self.bike_names:
#             if x==name:
#                 inp = int(input('Enter the number of days: '))
#                 bill = inp*500
#                 print(bill)
#                 insurance = input('Do you want to go for insurance 200 per/day. Enter True/False: ')
#                 if insurance=="True":
#                     insurance_amount = inp*200
#                     print("Final Price: ",bill+insurance_amount)

#                 confirmation = int(input('Enter 1 to confirm: '))
#                 if confirmation==1:
#                     if inp>5:
#                         bill -= 500
#                     print('Booking Confirmed')
#                     print('Bike Name:',name)
#                     print('Amount:',bill)
#                 else:
#                     print('Booking Cancelled')

# ob = Users()

# ob.prices()

# ob.book_vehicle()



# class Message:

#     message_id = 1

#     def __init__(self, sender, receiver, content):

#         self.id = message_id

#         self.sender = sender

#         self.receiver = receiver

#         self.content = content

#         message_id += 1

#     def display(self):

#         print("ID:", self.id)
#         print("Sender: ", self.sender)
#         print("Receiver:", self.receiver)
#         print("Content:", self.content)

# class Person:

#     def __init__(self, username):

#         self.username = username

#         self.sent_messages = []

#         self.received_messages = []


# class User(Person):

#     def send_message(self):

#         receiver_user = input("To whom would you like to send a message? ")

#         content = input("Enter your message: ")

#         sender_message = Message(self.username, receiver_user, content)

#         print("Message details")

#         sender_message.display()

#         self.sent_messages.append(sender_message)     


#     def show_inbox(self):

#         print("Your Inbox")

#         for i in range(len(self.received_messages)):

#             print(i)
    
#     def show_sent(self):

#         print("Your sent messages")

#         for i in range(len(self.sent_messages)):

#             print(i)


# class ChatSystem:

#     def __init__(self):

#         self.users = {}

#     def register_user(self):

#         username = input("Enter new username: ")
    
#         if username in self.users:

#             print("Username already exists!")
#             return

#         new_user = User(username)

#         self.users[username] = new_user

# def remove_element(list, target):

#     new_list = []

#     if target in list:

#         for i in list:
            
#             if i != target:

#                 new_list.append(i)
    
#         print(new_list)

#     else:

#         print("Element not found")
    


# li = [10, 20, 30, 40, 50, 60, 100, 140]

# target = int(input("Enter the target: "))

# remove_element(li, target)



# li = [30, 10, 20, 50, 40, 100, 70]

# sorted = False

# while not sorted:

#     swapped = False

#     for i in range(len(li)-1):

#         if li[i] > li[i+1]:
            
#             temp = li[i]
#             li[i] = li[i+1]
#             li[i+1] = temp

#             swapped = True

#     if not swapped:

#         sorted = True

# print(li)


# words = [ "Chennai", "Bangalore", "Pune", "Delhi", "Kolkata" ]

# uppercase_words = [x.upper() for x in words ]

# print(uppercase_words)


# celcius = [ 20, 30, 35, 40]

# farenheit = [(x*9/5)+32 for x in celcius]


# emails = ["user1@gmail.com","abcd","admin@yahoo.com","hello","alpha@hotmail.com","dummy","kabir@intellipaat.in"]

# valid_emails = [x for x in emails if "@" in x]

# print(valid_emails)



# li = ["apple", "banana", "guava", "pineapple", "kiwi"]

# li_length = [len(x) for x in li]

# print(li_length)



# li = ["Apple", "Banana", "Guava", "Pineapple", "Kiwi"]

# li_2 = [(x.upper(),len(x)) if len(x) > 5 else (x.lower(),len(x)) for x in li]

# print(li_2)



# even_squares = { x : x**2 for x in range(2,21,2)}

# print(even_squares)

# numbers = (x for x in range(10))

# print(numbers)


# original = {1:10,2:15,3:7}

# modified = {x : original[x] for x in original if original[x]>10}

# print(modified)


# marks = [85,42,77,30,48,93,51]

# results = { x : "Pass" if x >= 50 else "Fail" for x in marks}

# print(results)



# word = "Programming"    

# filtered = {x for x in word if x in "aeiou"}

# print(filtered)


# try: 

#     a = int(input("Enter first number: "))

#     b = int(input("Enter second number: "))
    
#     print(a/b)

# except ZeroDivisionError:
#     print("Cannot divide number by 0")

# except ValueError:
#     print("Incorrect value entered")

# else:
#     print("No erros found")

# finally: 
#     print("Process end")


# try: 
    
#     number = int(input("Enter a number: "))

#     is_prime = True

#     if number < 0:
#         raise ValueError("Value cannot be negative")
    
#     elif number < 2:
#         raise ValueError("Invalid number. Enter a value greater than 2")

#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 is_prime = False
#                 break
    
#         if is_prime:
#             print("The number is a Prime number")
        
#         else:
#             print("The number is not a Prime number")


# except Exception as e: 

#     print("Error: ",type(e).__name__)




# class LowFundError(Exception):
#     def __init__(self,message):
#         super().__init__(message)
    
# class InvalidAmount(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# balance = 10000
# money_withdraw = int(input('Enter the amount you want to withdraw: '))

# if money_withdraw % 100 != 0:
#     raise InvalidAmount('Invalid amount. Enter amount in multiples of 100.')
# else:
#     print('Withdraw successful')

# if money_withdraw>balance:
#     raise LowFundError('Insufficient funds to withdraw')
# else:
#     print('Withdraw succesfull')


# while True:
#     try:
#         marks = int(input("Enter marks of the student: "))

#         if marks < 0 or marks > 100:
#             raise ValueError("Invalid input, enter marks from 0 to 100")
        
#         else:
#             print("Marks of the student: ", marks)
#             break
    
#     except Exception as e:
#         print("Error: ", type(e).__name__)
    

# class InvalidQuantityError(Exception):
#     def __init__(self):
#         super().__init__("Cart must have 1 or more items")

# class OutOfStockError(Exception):
#     def __init__(self):
#         super().__init__("Entered value is greater than stock")


# stock = 20

# try:
#     items = int(input("Enter number of items you'd like to purchase: "))

#     if items < 1:
#         raise InvalidQuantityError()
    
#     if items > stock:
#         raise OutOfStockError()

# except Exception as e:
#     print("Error occured: ", e)



# Write a program to create valid user_id and password
# Constraints are:
# list = ['omega23','minion45','giant13','kolin32']
# user_id should not contain any special characters, and make sure it's not same as any existing id
# password: it should be all +ve integers and length must me min of 8 digits. 
# if the constrains does not meet your program must raise an error. 


# class UserAlreadyExists(Exception):
#     def __init__(self, message):
#         super().__init__(message)
    

# class SpecialCharactersError(Exception):
#     def __init__(self, message):
#         super().__init__(message)


# class PasswordTooShort(Exception):
#     def __init__(self, message):
#         super().__init__(message)



# li = ['omega23','minion45','giant13','kolin32']

# special_chars = "!@#$^&*()|?\\/][}{]~"

# try:
#     new_user = input("Enter new User ID: ")

#     if new_user in li:
#         raise UserAlreadyExists("This User ID already exists.")
    
#     for i in range(len(new_user)):
#         if new_user[i] in special_chars:
#             raise SpecialCharactersError("The User ID cannot contain special characters.")
    
#     password = int(input("Enter password: "))

#     if len(str(password)) < 8:
#         raise PasswordTooShort("The password is too short. Min length: 8 digits.")

# except ValueError:
#     print("Password must contain only digits")

# except Exception as e:
#     print("Error: ", e)


# li = [x for x in range(1,21)]

# li2 = []

# for i in range(len(li)): # for i in li
#     li2.append(i**2)

# dict = {x : x**2 for x in range (1,11)}

# for i in dict:
#     print(i, ": ", dict[i])


# s1 = {x for x in range(1,21) if x % 2 == 1}

# for i in s1:
#     print(i)

# print(type(s1))

# a = [[1,2],[3,4],[5,6],[7,8]]

# for i in a:
#     for j in i:
#         print(j)


# a = {1:{'one':1}, 2: {'two':2}, 3: {'three':3}}

# num = 1

# while num < 101:
#     if num % 2 == 0:
#         print(num)
    
#     num += 1

# x = 1

# while x < 6:
#     print(x*3)
#     x += 1


# li = {x : x**3 for x in range(1,11)}

# range = 1

# while range <= len(li):
#     print(range, ": ", li[range])
#     range += 1



# for i in range(21):

#     if i % 10 == 0:
#         continue
    
#     if i == 18:
#         break

#     if i % 2 == 0:
#         print(i)

#     elif i % 2 == 1:
#         pass
    
    
# for i in range(5):
#     print(" " * (5-i), "*")



# 1. Print all the leap years between 1990 and 2050

# import time

# from datetime import date, time, datetime

# import calendar

# print("Leap years from 1990 to 2050")
# for i in range(1990, 2051):
#     if calendar.isleap(i):
#         print(i)

# # 2. What day of the week was 15th August 1947

# aug_15_1947 = date(1947, 8, 15)

# print("August 15, 1947: ")
# print(calendar.day_name[calendar.weekday(1947, 8, 15)])


# # 3. 

# day = int(input("Enter birthday day: "))
# month = int(input("Enter birthday month: "))
# year = int(input("Enter birthday year: "))

# birthday = calendar.weekday(year, month, day)

# if birthday == 5 or birthday == 6:
#     print("Your birthday falls on a weekend")

# else:
#     print("Your birthday is on a weekday")

# import sqlite3

# connection = sqlite3.connect("first_database.db")

# cur = connection.cursor()

# rows = [
#     "insert into students (name, grade) values ('Kartik',92.5)",
#     "insert into students (name, grade) values ('Rahul',87.9)",
#     "insert into students (name, grade) values ('Anjali',97.9)",
#     "insert into students (name, grade) values ('Shyam',77.2)"
# ]

# for x in rows:
#     cur.execute(x)

# print("\ngrade between 80 and 90:")

# for x in cur.execute('select * from students where grade between 80 and 90'):
#     print(x)

# print("\nname with s or grade > 95:")
# for x in cur.execute('select * from students where name like "%s%" or grade > 95'):
#     print(x)

# print("\nstudents with grade < 90:")
# for x in cur.execute('select name from students where grade < 90'):
#     print(x)


import asyncio

# async def say_hello(name):
#     print("Hello, ", name)
#     await asyncio.sleep(2)
#     print("Goodbye, ", name)

# async def hello_goodbye():
#     await asyncio.gather(
#         say_hello("Amar"),
#         say_hello("Akbar"),
#         say_hello("Anthony")
#     )

# asyncio.run(hello_goodbye())


# async def countdown(n, name):

#     for i in range(n, 0, -1):
#         print(i)
#         await asyncio.sleep(1)
    
#     print(name, " Complete!")

# async def timers():
#     await asyncio.gather(
#         countdown(10, "timer 1"),
#         countdown(5, "timer 2")
#     )

# asyncio.run(timers())
 
# import time


# async def task_run(name, n):

#     print(name, " started!")

#     await asyncio.sleep(n)

#     print(name, " completed!")

# async def tasks():
#     await asyncio.gather(
#         task_run("task1",1),
#         task_run("task2",2),
#         task_run("task3",3)
#     )


# start = time.time()

# asyncio.run(tasks())

# end = time.time()

# print("total time: ", end-start)


# import multiprocessing

# from multiprocessing import Pool
# def square(x):
#     # print("Square of",x,"=",x*x)
#     return x**2


# numbers = [1,2,3,4,5]

# with Pool(processes=2) as p: # It will create 2 processes (workers)
#     results = p.map(square,numbers)

# print(results)
    

import re

# words = "magnify classify scatter flying lying"

# print(re.findall(r"fy",words))


# string = "abs23, a32b1be33, fd78320r212n3, 3b30dm11"

# print(re.findall(r"\d\d",string))

# spaces = "We are learning Regular Expressions which is also known as Regex."

# print(len(re.findall(r"\s",spaces)))

emails = ["test@example.com", "kartik@domain.org" , "invalid.email@com"]
# ^ -> words 
# [\w\.]
# +
pattern = r"^[\w\.]+@[\w\.]+\.\w{2,}$"
for x in emails:
    print(x, bool(re.match(pattern,x)))