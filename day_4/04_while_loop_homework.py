#%%
# ---------------------------------------------------------
# HOMEWORK 4: WHILE LOOP 🔁
#%%
# ---------------------------------------------------------


#%%
# TASK 1: Guess the Number Game
# Store a secret number (e.g. 42).
# Keep asking the user to guess until they get it right.
# After each wrong guess, tell them if they're too high or too low.
# Count the number of attempts and print it when they win.
# Use int(input(...)) to get the guess.
# Write your code below:

secret_number = 42
attempts = 0

print("Welcome! Can you find the secret number?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Correct! It took you {attempts} attempts.")
        break 
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")


#%%
# TASK 2: Number Collector
# Keep asking the user for a positive number.
# If they enter 0 or a negative number, stop.
# After stopping, print:
#   - All numbers collected (as a list)
#   - The total
#   - The largest number entered
# Hint: build a list inside the loop using .append()
# Write your code below:

numbers = []
total = 0

while True:
    number = int(input("Enter a positive number (or 0/negative to stop): "))
    
    if number <= 0:
        break 
        
    numbers.append(number)
    total += number

if len(numbers) > 0:
    print(f"All numbers: {numbers} | Total: {total} | Largest: {max(numbers)}")
else:
    print("No positive numbers were entered.")


#%%
# TASK 3: Simple ATM
# Set a balance of Rs. 10000.
# Show a menu each round:
#   1. Check balance
#   2. Withdraw
#   3. Deposit
#   4. Exit
# Keep showing the menu until the user picks Exit.
# For withdraw: check that they don't go below Rs. 0.
# Use a while True loop with break to exit.
# Write your code below:

balance = 10000

while True:
    choice = int(input("1. Check balance\n2. Withdraw\n3. Deposit\n4. Exit\n\nSelect an option: "))
    
    if choice == 1:
        print(f"Balance is {balance}")
    elif choice == 2:
        withdraw_amount = int(input("Enter withdraw amount"))
        if balance > 0 and withdraw_amount <= balance: balance -= withdraw_amount
        else: print("insufficient funds")
    elif choice == 3:
        balance += int(input("Enter deposit amount"))
    elif choice == 4:
        break
    else:
        print("Choose correctly!")


#%%
# ⭐ BONUS CHALLENGE:
# Build a simple number quiz game.
# Generate 5 random multiplication questions (e.g. "What is 7 × 8?").
# Give the user 2 attempts per question.
# Track the score and print it at the end.
# Hint: use the random module:
#   import random
#   a = random.randint(1, 10)
#   b = random.randint(1, 10)
# Write your code below:
