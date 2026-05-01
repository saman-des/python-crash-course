#%%
# ---------------------------------------------------------
# HOMEWORK 5: break & continue 🎮
#%%
# ---------------------------------------------------------


#%%
# TASK 1: First Negative
# Create a list of numbers: [10, 25, 8, -3, 14, -7, 20]
# Use a for loop with break to find and print the FIRST negative number.
# Print: "First negative number: -3"
# If no negative number is found, print "No negative numbers."
# Hint: use a found = False flag before the loop.
# Write your code below:


numbers = [10, 25, 8, -3, 14, -7, 20]
found = False

for i in numbers:
    if i < 0:
        print(f"First negative number {i}")
        found = True
        break

if found == False: print("No negative numbers")


#%%
# TASK 2: Skip the Banned Words
# Create a list of words including some "banned" ones:
# ["hello", "spam", "world", "click", "python", "buy", "now"]
# Banned words: ["spam", "click", "buy"]
# Use continue to skip banned words and print only the allowed ones.
# Write your code below:

words = ["hello", "spam", "world", "click", "python", "buy", "now"]
banned = ["spam", "click", "buy"]

for w in words:
    if w in banned:
        continue
    print(w)



#%%
# TASK 3: Input Validator
# Ask the user for a number between 1 and 10.
# Keep asking (while True + break) until they give a valid number.
# Once valid, print: "Great! You entered: 7"
# If the input is not a number at all, print "That's not a number!"
# and keep asking.
# Write your code below:

while True:
    user_input = input("Enter a number between 1 and 10: ")
    
    if user_input.isdigit():
        num = int(user_input)
        
        if 1 <= num <= 10:
            print(f"Great! You entered: {num}")
            break
        else:
            print("Out of range! Please enter 1 to 10.")
            
    else:
        print("That's not a number!")


#%%
# ⭐ BONUS CHALLENGE:
# Predict the output of each loop BEFORE running it.
# Write your prediction as a comment, then run to verify.

# Loop A:
for i in range(1, 8):
    if i % 2 == 0:
        continue
    if i > 5:
        break
    print(i)
# Your prediction: ?

# Loop B:
total = 0
for n in [10, 20, 30, 40, 50]:
    if total >= 50:
        break
    total += n
print(total)
# Your prediction: ?
