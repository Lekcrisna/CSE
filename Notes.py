# print("Hello World!")

# crisna(use ctrl / to toggle comments)

# print(3 + 5)
# print(5 -3 )
# print(5 * 3)
# print(6 / 2)
# print(3 ** 2)
#
# print() # creates a blank line
# print("See if you can figure this out")
# print(13 % 15 )

# Variable
# car_name = "Thomas the dank engine"
# car_type = "Train"
# car_cylinders = 8
# car_mpg = 9000.1
#
# # Inline Printing
# print("My car is the %s" % car_name)
# print("My car is the %s. It is a %s" % (car_name,car_type))

# Taking input
# name = input("What is your name?")
# print("Hello %s." % name)
# print(name)

# age = input("How Old Are You")
# print("%s cool beans." % age)


# def print_hw():
#     print("Hello World")


# print_hw()


# def say_hi(name): #Name is a "parameter"
#     print("Hello %s." % name)
#     print("I hope you have a fantastic day.")


# say_hi("John")


# def birthday(age):
#     age +=1 # age = age + 1
#     print(age)

# say_hi("John")
# print("John is 15. Next Year:")
# birthday(15)
#
# Press Ctrl-A and Crtl-/
# to comment old code

# def f(x):
#     return x**5 + 4 * x**2 + 4 - 17*x**2 + 4


# print(f(3))
# print(f(3) + f(5))

# if statements


# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80: #Else if
#         return "B"
#     elif percentage >=70:
#         return "C"
#     elif percentage >=60:
#         return "D"
#     else:
#         return "F"

#Loops


# for num in range(5):
#     print(num + 1)
#
# for mystery in "Hello World":
#     print(mystery)

# a = 1
# while a < 10:
#     print(a)
#     a+= 1
#
# response = ""
# # while response != "Hello":
# #     response = input("Say \"Hello\"")
#
# print("Hello \nWorld") #\n means a newline
#
# import random # IMPORTS should be at the top
# print(random.randint(0,6))


#camparisons
# print(1 == 1)  #Two equal to compare
# print(1 != 2)  #One is not equal to 2
# print (not False)  #This prints true
# print(1 == 1 and 4 <= 5)
# print(1 < 0 or 5  > 1)


#Recasting
# c = '1'
# print(c == 1)  #False - C is a string, 1 is an interger
# print(int(c) == 1)  #True - compares two ints
# print(c == str(1))  #True - Compare two strings

#list
# the_count = [1, 2, 3, 4, 5]
# cheeseburger_ingredients = ['cheese', "beef", "sauce", "sesame seed bun", "avocado", "onion"]
# print(cheeseburger_ingredients[0])
# print(len(cheeseburger_ingredients))



#Recasting into a list
# strOne = "Hello World!"
# listOne = list(strOne)
# print(listOne)
# listOne[11] ='.'
# print(listOne)

# adding things to a list
# cheesburger_ingredients.append("Fries")
# print(cheesburger_ingredients)
# cheeseburger_ingredients.append("lettuce")
# print(cheeseburger_ingredients)

# removing things from a list
# cheeseburger_ingredients.pop(1)
# print(cheesburger_ingredients)
# cheesburger_ingredients.remove("cheese")
# print(cheeseburger_ingredients)

# Getting the alphabet
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.punctuation)

# Making things lowercase
# strTwo = "ThIs iS a VeRY oDd sEntENcE"
# lowercase = strTwo.lower()
# print(lowercase)

# L1 = ['h', 'e', 'l', 'l', 'o']
#     .join(L1)


#Dictionaries -  Made up of key values pair

dictionary ={"name": 'Lance', 'age': 26, 'height': 6 * 12 + 6}

# Accessing things from a dictionary
print(dictionary['name'])

