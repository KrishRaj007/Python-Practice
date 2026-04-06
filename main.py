# #string
# first_name = "Krish"
# food = "Burger"
# email = "krish.r2106@gmail.com"

# #integers
# age = 18
# quantity = 5
# no_of_students = 50

# #float
# price = 11
# cgpa = 8.2
# distance = 500

# #boolean
# is_online = True
# is_student = False

# name = "Krish Raj"
# age = 18
# gpa = 7.7
# is_student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(is_student))
# ----------------------------------------------------------------------------------- data types

# name = input("Enter your Name: ")
# age = int(input("Enter your age: "))

# print(f"Hello {name}")
# print(f"You're {age} yrs old")
# -----------------------------------------------------------------------------------

# friends = 3

# friends += 1
# friends = friends + 1          #argumented assignment operator
# friends -= 1 
# friends = friends - 1           #subtraction Operator
# friends *= 5 
# friends = friends * 5              #multiplication operator
# friends /= 4 
# friends = friends / 4             #division operator
# friends **= 2 
# friends = frineds ** 2            #exponential operator
# friends //= 1 
# friends = friends //2                #Floor Division

# -----------------------------------------------------------------------------------arithmetic operators
# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 5)
# result = max(x, y,z)
# result = min(x, y, z)
# print(result)
# ----------------------------------------------------------------------------------- built-in functions

# import math

# x = 10.99

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
# print(result)
# ----------------------------------------------------------------------------------- math module

# age = int(input("Enter the age: "))

# if age >= 18:
#     print("You're signed in!")
# elif age < 0:
#     print("You haven't been borned yet!")
# elif age >= 100:
#     print("Damn! You are so old for signing up")
# else:
#     print("You must be 18+ to sign in.")
# -----------------------------------------------------------------------------------  if/elif/else statements

# x if condition else y                      Formula

# num = 9
# a = 6
# b =7
# age = 16
# temp = 31
# user_role = "xyz"

# print("positive" if num > 0 else "negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# temp = "Hot" if temp > 30 else "Cold"
# role = "Admin" if user_role == "admin" else "Guest"
# -----------------------------------------------------------------------------------  Conditional Expression

# name = input("Enter Your Full Name: ")
# phone = input("Enter Your Phone Number: ")

# result  = len(name)
# result = name.find(" ")
# result = name.rfind("r")
# name = name.capitalize()
# name = name.lower()
# result = name.isalpha()
# result = phone.count("7")
# phone = phone.replace("", "-")
# ----------------------------------------------------------------------------------- String Methods

# credit_number = "1234-5678-9012-3456"

# print(credit_number[4])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2])
# credit_number = (credit_number[::-1])
# ----------------------------------------------------------------------------------- String Indexing

# price1 = 12.54089
# price2 = -987.36
# price3 = 1236.789

# print(f"The Price 1 is {price1: .2f}")
# print(f"The Price 2 is {price2: .2f}")                #Decimal Precision
# print(f"The Price 3 is {price3: .2f}")

# print(f"The Price 1 is ${price1:10}")
# print(f"The Price 2 is ${price2:10}")                   #Paddng
# print(f"The Price 3 is ${price3:10}")

# print(f"The Price 1 is ${price1:>10}")
# print(f"The Price 2 is ${price2:>10}")                   #Right-Justify
# print(f"The Price 3 is ${price3:>10}")

# print(f"The Price 1 is ${price1:<10}")
# print(f"The Price 2 is ${price2:<10}")                   #Left-Justify
# print(f"The Price 3 is ${price3:<10}")

# print(f"The Price 1 is ${price1:^10}")
# print(f"The Price 2 is ${price2:^10}")                   #Centre-Justify
# print(f"The Price 3 is ${price3:^10}")

# print(f"The Price 1 is ${price1:,}")
# print(f"The Price 2 is ${price2:,}")
# print(f"The Price 3 is ${price3:,}")
#                                                           #Comma Sperator
# print(f"The Price 1 is ${price1:,.2f}")
# print(f"The Price 2 is ${price2:,.2f}")
# print(f"The Price 3 is ${price3:,.2f}")
# -----------------------------------------------------------------------------------Python Format Specifiers

# name = input("Enter your Name: ")

# while name == "":
#     print("You didn't type anything.")
#     name = input("Enter your Name: ")                     #While Loop

# print(f"Hello {name}")



# name = input("Enter your Name: ")

# while name == "":
#     print("You didn't type anything.")                   #Infinite Loop
    

# print(f"Hello {name}")
# -----------------------------------------------------------------------------------While Loops

# for x in range(1, 11):
#     print(x)                                               #For Loop Basics


# for x in reversed(range(1, 11)):
#     print(x)                                               #Reversed For Loop



# for x in range(1, 11, 3):
#     print(x)                                               #For Loop Over Some Steps


# credit_card_number = "1234-5678-9012-3456"

# for x in credit_card_number:                               #For Loop For Some Strings
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue                                            #Continue For Loop
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break                                            #Break For Loop
#     else:
# -----------------------------------------------------------------------------------For Loops

# for x in range(1, 10):
#         print(x, end = " ")                              #Nested Loop Basics


# for x in range(3):
#         for y in range(1, 10):                          #Nested Loops #2       
#                 print(y, end = " ")

# for x in range(3):
#         for y in range(1, 10):
#                 print(y, end  = " ")                    #Nested Loop #3
#         print()
#  -----------------------------------------------------------------------------------Nested Loops

# fruits = ["Apple", "Banana", "Guava", "Mango"]
# print(fruits)                                             #List
# print(fruits[3])                                          #List for accessing a specific value
# print(fruits[::-1])                                       #List running backwards
# print(fruits[::2])                                        #List for selecting elements one skipping at a time
# for fruit in fruits:                                      #List using For Loop
#     print(fruit)
# print(len(fruits))                                        #Total number of elements in a List
# print("Apple" in fruits)                                  #Boolean value of thelist element
# fruits[3] = "Pineapple"

# for fruit in fruits:                                      #For replacing an element in a List
#     print(fruit)
# fruits.append("Pineapple")
# print(fruits)                                             #For adding an element in a List
# fruits.remove("Apple")
# print(fruits)                                            #For removing an element in a List
# fruits.insert(4, "Pineapple")
# print(fruits)                                             #For inseting a value as well as indexing it
# fruits.sort()                                             #Sorting of list in an Alphabetical Order
# fruits.reverse()                                          #Reversing the order of the list
# fruits.sort()
# fruits.reverse()                                           #Reversing the order of the ordered list
# fruits.clear()                                             #Clear the elements of the list
# print(fruits.index("Apple"))                               #To print the index value of the element in the list
# print(fruits.count("Mango"))                               #To count the number of the value it repeat itself
#  -----------------------------------------------------------------------------------Lists

# fruits = {"Apple", "Mango", "Grapes", "Banana"}
# print(fruits.add("Orange"))
# print(fruits.remove("Grapes"))
# print(fruits.pop())
# print(fruits.clear())
# print(fruits)
#-----------------------------------------------------------------------------------Sets

# fruits = ("Apple", "Orange", "Mango", "Pineapple")
# print(len(fruits))
# print("Pineapple" in fruits)
# print(fruits.index("Pineapple"))
# print(fruits.count("Apple"))
# for fruit in fruits:
    # print(fruit)
#-----------------------------------------------------------------------------------Tuple

# capitals = {"India": "New Delhi", 
#             "Japan": "Tokyo", 
#             "France": "Paris",
#             "China": "Beijing",
#             "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))                    #For getting the value using a key

# if capitals.get("Japan"):                       #Using the same thing but with the IF statement
#     print("This capital exists")
# else:
#     print("This capital doesn't exist")

# capitals.update({"USA": "Washington D.C."})            #Adding a new value
# capitals.update({"China": "New Jersey"})                 #Changing the value of an existing key
# capitals.pop("India")                                    #For removing the first key-value pair from the dictionary
# capitals.popitem()                                      #For removing the latest key-value ppair from the dictionary
# capitals.clear()                                       #For clearing the Dictionary
# print(capitals)

# keys = capitals.keys()                               #For finding the value of keys only

# for keys in capitals.keys():                       #Same method but with the help of for loop
    # print(keys)

# values = capitals.values()                        #For finding the value of key-value pairs only

# for values in capitals.values():                  #Same method but with the help of for loop
#     print(values)

# item = capitals.items()                         #Representss 2D list of tuples.... It looks like [(), (), ()]

# for keys, values in capitals.items():             
    # print(f"{keys}: {values}")                            #Same method but with the help of for loop
#-----------------------------------------------------------------------------------------------------------------------Dictionaries

# def function(name, age):
#     print(f"Happy Birthday to {name}")
#     print(f"You are {age} years old")
#     print("Happy Birthday to you")
#     print()


# function("Krish", 18)
# function("Bro", 19)
# function("Bro2", 17)

# def display_invoice(username, amount, due_date):
#     print(f"Hello, {username}")
#     print(f"Your billing amount is {amount}, which is due on {due_date}")                 #Example for functions

# display_invoice("Krish", 12100, "17/04")


# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def division(x, y):
#     z = x / y
#     return z                                                      #Return Statement practise

# print(add(5, 3))
# print(subtract(5, 3))
# print(multiply(5, 15))
# print(division(5, 1))

# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return  first + " " + last

# full_name = create_name("krish", "raj")
# print(full_name)
# ---------------------------------------------------------------------------------------------------------------------------Functions

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(10000))
# print(net_price(20000, 0.1))
# print(net_price(15000, 0.1, 0))
# ----------------------------------------------------------------------------------------------------------------------------Default Arguments

# def hello(greetings, title, first, last):
#     print(f"{greetings}, {title} {first} {last}")

# hello(first="Krish", title="Master", greetings="Hello", last="Raj")
# -----------------------------------------------------------------------------------------------------------------------------Keyword Arguments

def add(*args):
    total = 0
    for arg in args:
        total += arg 