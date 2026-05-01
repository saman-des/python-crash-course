#%%
# ---------------------------------------------------------
# HOMEWORK 2: range() 🔢
#%%
# ---------------------------------------------------------


#%%
# TASK 1: Multiplication Table
# Ask the user for a number.
# Print its multiplication table from 1 to 12.
# Format: "7 × 1 = 7"
# Use range(1, 13).
# Write your code below:

number = int(input("Enter number"))

for i in range(1,13):
    print(f"{number} * {i} = {number * i}")


#%%
# TASK 2: Sum of Numbers in a Range
# Ask the user for a start and end number.
# Using range(), calculate the sum of ALL integers from start to end (inclusive).
# Print the result.
# Example: start=1, end=10 → sum = 55
# Write your code below:

start, end = map(int, input("Enter 2 numbers").split())
total = 0

for i in range(start, end +1):
    total += i

print(f"Total sum is {total}")


#%%
# TASK 3: Rocket Countdown
# Using range() with a NEGATIVE step, print a countdown from 10 to 1,
# then print "Liftoff! 🚀"
# Write your code below:

for i in range(10,1, -1):
    print(f"Liftoff! 🚀")



#%%
# ⭐ BONUS CHALLENGE:
# Print all numbers from 1 to 100 that are divisible by BOTH 3 and 7.
# Hint: a number divisible by 3 means: number % 3 == 0
# Use range() and an if condition inside the loop.
# Write your code below:
