# Returning Multiple Values 
# Program 3
# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple
# Do a function that can return multiple values
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

print("Apple E-Store")

def get_purchase():
    money_ = int(input("Enter your money: "))
    apple_price = int(input("Enter apple price: "))
    qty_ = (money_ / apple_price)
    convert_ = (qty_ * apple_price)
    change_ = (convert_ - money_) 

def display(money_, apple_price, qty_, convert_, change_):
    print("You can buy", convert_, "apples and your change is ₱", change_)

money_, apple_price, qty_, convert_, change_ = get_purchase()
display(money_, apple_price, qty_, convert_, change_)