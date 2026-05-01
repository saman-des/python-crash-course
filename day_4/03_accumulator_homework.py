#%%
# ---------------------------------------------------------
# HOMEWORK 3: ACCUMULATOR PATTERN 🪣
#%%
# ---------------------------------------------------------


#%%
# TASK 1: Average Calculator
# Create a list of at least 6 exam scores.
# Use a for loop to:
#   1. Calculate the total (sum of all scores)
#   2. Calculate the average (total / number of scores)
# Print both the total and the average.
# Do NOT use the built-in sum() function — use the loop pattern!
# Write your code below:

scores = [85, 92, 78, 95, 88, 71]
total = 0

for i in scores:
    total += i

average = total / len(scores)

print(f"Sum {total} | Average {average}")


#%%
# TASK 2: Count Vowels
# Write a program that asks the user for a word.
# Loop through each letter and count how many vowels (a, e, i, o, u) it has.
# Print: "The word 'python' has 1 vowel(s)."
# Hint: check if each letter is 'in' the string "aeiou"
# Write your code below:

word = input("Enter a word")
vowels = 0

for i in (word):
    if i in {'a', 'e', 'i', 'o', 'u'}:
        vowels += 1

print(f"Vowels = {vowels}")




#%%
# TASK 3: Filter a List
# Create a list of at least 8 numbers (mix of positive and negative).
# Use a for loop to build TWO new lists:
#   positives = all numbers >= 0
#   negatives = all numbers < 0
# Print both lists after the loop.
# Write your code below:

# Create a list of 8 numbers
numbers = [12, -7, 0, 45, -100, 3, -1, 22]

# Initialize two empty lists to hold our filtered results
positives = []
negatives = []

# Loop through the numbers
for num in numbers:
    if num >= 0:
        positives.append(num)  # Add to positives if zero or higher
    else:
        negatives.append(num)  # Add to negatives if less than zero

# Print the final lists
print(f"Positive numbers: {positives}")
print(f"Negative numbers: {negatives}")



#%%
# ⭐ BONUS CHALLENGE:
# Ask the user to enter names one at a time.
# Keep asking "Enter a name (or 'done' to finish): "
# Use a while loop and add each name to a list.
# When they type 'done', stop and print:
#   - The complete list of names
#   - How many names were entered
#   - The names sorted alphabetically (use sorted())
# Write your code below:
