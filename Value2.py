# Returning Multiple Values 
# Program 2
# Create a program that will ask how many apples and oranges you want to buy but with a function that can return multiple values
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount of the apples and oranges that you bought is ______.
print("Apple and Orange E-Commerce")

apple_price = 20
orange_price =25

def get_exchange():
    apple_qty = int(input("Enter the quantity of apple: "))
    orange_qty = int(input("Enter the q4uantity of orange: "))
    total_apple = (apple_qty * apple_price)
    total_orange = (orange_qty * orange_price)
    total_ = (total_orange + total_apple)
    return apple_qty, orange_qty, total_apple, total_orange, total_

def display_(apple_qty, orange_qty, total_apple,total_orange,total):
    print("The total amount of the apples and oranges that you bought is", total)

apple_, orange_, ttl_apple, ttl_orange, ttl_ = get_exchange()
display_(apple_, orange_, ttl_apple, ttl_orange ,ttl_)