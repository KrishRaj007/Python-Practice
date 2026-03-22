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
#                 print(y, end  = " ")                      #Nested Loop #3
#         print()