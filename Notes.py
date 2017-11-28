print("Hello World!")

# crisna(use ctrl / to toggle comments)

print(3 + 5)
print(5 -3 )
print(5 * 3)
print(6 / 2)
print(3 ** 2)

print() # creates a blank line
print("See if you can figure this out")
print(13 % 15 )

# Variable
car_name = "Thomas the dank engine"
car_type = "Train"
car_cylinders = 8
car_mpg = 9000.1

# Inline Printing
print("My car is the %s" % car_name)
print("My car is the %s. It is a %s" % (car_name,car_type))

# Taking input
# name = input("What is your name?")
# print("Hello %s." % name)
# print(name)

# age = input("How Old Are You")
# print("%s cool beans." % age)


def print_hw():
    print("Hello World")


print_hw()


def say_hi(name): #Name is a "parameter"
    print("Hello %s." % name)
    print("I hope you have a fantastic day.")


say_hi("John")


def birthday(age):
    age +=1 # age = age + 1
    print(age)

say_hi("John")
print("John is 15. Next Year:")
birthday(15)