#%%
# ---------------------------------------------------------
# HOMEWORK 1: FOR LOOP BASICS 🔄
#%%
# ---------------------------------------------------------


#%%
# TASK 1: Your Favourite Things
# Create a list of 5 things you like (foods, games, anything!).
# Use a for loop to print each one on its own line like this:
# "I really like: pizza"
# Write your code below:

favorite_things = ["Pizza", "Chess", "Coding", "Hiking", "Coffee"]

for thing in favorite_things:
    print(f"I really like: {thing.lower()}")

#%%
# TASK 2: Length Reporter
# Create a list of at least 5 words.
# Loop through the list and for each word print:
# "banana → 6 letters"
# Hint: use len() inside the loop.
# Write your code below:

words = ["Pizza", "Chess", "Coding", "Hiking", "Coffee"]

for i in words:
    print(f"{i} -> {len(i)} letters")



#%%
# TASK 3: Shopping Bill
# Create a list of at least 5 item prices (as numbers).
# Loop through them and print each price, then after the loop
# print the total.
# Use the accumulator pattern: start total = 0, add each price.
# Write your code below:
prices = [12.99, 5.50, 42.00, 8.75, 120.00]
total =0

for i in prices:
    print(f"Price is Rs. {i}")
    total += i

print(f"Total is Rs.{total}")



#%%
# ⭐ BONUS CHALLENGE:
# Create a list of temperatures in Celsius:
# [0, 20, 37, 100, -10]
# Loop through and convert each to Fahrenheit: F = (C × 9/5) + 32
# Print: "0°C = 32.0°F"
# Write your code below:
