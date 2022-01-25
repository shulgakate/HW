# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
# Generate 100 random numbers between 0 and 1000
randomNumbers = random.sample(range(0, 1000), 100)
print("The unsorted list is: ", randomNumbers)

# Bubble sorting
# Outer loop
for i in range(len(randomNumbers) - 1):
    # Inner loop
    for j in range(len(randomNumbers) - 1):
        # If randomList[j] > randomList[j + 1] then inverse elements
        if randomNumbers[j] > randomNumbers[j + 1]:
            a = randomNumbers[j]
            randomNumbers[j] = randomNumbers[j + 1]
            randomNumbers[j + 1] = a

# Print sorted list
print("The sorted list is: ", randomNumbers)

# Calculate average for even and odd numbers
oddSum = oddCount = evenSum = evenCount = 0
for i in range(0, len(randomNumbers)):
    if randomNumbers[i] % 2 == 1:
        oddSum = oddSum + randomNumbers[i]
        oddCount: int = oddCount + 1
    else:
        evenSum = evenSum + randomNumbers[i]
        evenCount: int = evenCount + 1

# print both average result in console
print("Average of odd numbers: ", oddSum/oddCount)
print("Average of even numbers: ", evenSum/evenCount)
