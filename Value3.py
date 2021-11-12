# Returning Multiple Values 
# Program 3
# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple
# Do a function that can return multiple values
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can now buy ___ apples and your change is ___ pesos.

print("Apple E-Store")

def get_purchase():
    money_ = int(input("Enter your money: "))
    apple_price = int(input("Enter apple price: "))
    qty_ = int(money_ / apple_price)
    convert_ = int(qty_ * apple_price)
    change_ = int(money_ -  convert_) 
    return money_, apple_price, qty_, convert_, change_

def display(money_, apple_price, qty_, convert_, change_):
    print("You can now buy", qty_, "apples and your change is ₱", change_)

money__, apple__price, qty__, convert__, change__= get_purchase()
display(money__, apple__price, qty__, convert__, change__)