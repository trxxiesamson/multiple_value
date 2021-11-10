# Returning Multiple Values 
# Program 1
#Create a program that will ask for name, age and address but with a function that can return multiple values
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

print("This is your basic Introduction Machine")

def get_user_input():
    name_ = input("Tell me your name: ")
    age_ = int(input("How about your age? : "))
    add_ = input("Where do you live? : ")
    return name_, age_, add_

def display(name_, age_, add_):
    print("Hello! My name is", name_,". I am currently", age_," years old and I am residing at", add_)

# Steps
# 1. Ask for the name, age, and address then save as variable
name, age , add = get_user_input()
# 2. Display the name, age, and address
display(name, age, add)