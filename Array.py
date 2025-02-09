# 1. Write a program to print all the numbers from the given array using a loop.
# L = {23, 45, 32, 25, 46,33, 71, 90}

L = {23, 45, 32, 25, 46, 33, 71, 90}

# Convert set to list to maintain order (optional)
L = list(L)

# Using a for loop to print each number
for number in L:
    print(number)


# 2. Write a program to reverse the array and print the reversed array.


L = [23, 45, 32, 25, 46, 33, 71, 90]
L.reverse()
print("Reversed array:", L)


# 3. Write a program to take the size of the array,
# array and target as input from the user and check whether the target exists in this array or not.

# Take the size of the array from the user
size = int(input("Enter the size of the array: "))

# Take array elements as input from the user
L = []
print(f"Enter {size} elements:")
for _ in range(size):
    L.append(int(input()))

# Take the target number from the user
target = int(input("Enter the target number: "))

# Check if the target exists in the array
if target in L:
    print("Target exists in the array.")
else:
    print("Target does not exist in the array.")



# 4. Write a program to take N numbers from a user as input and then print the duplicates in 
# those N numbers. Also, take N as an input from the user.

# Take the size of the array from the user
N = int(input("Enter the number of elements: "))

# Take N numbers as input from the user
L = []
print(f"Enter {N} numbers:")
for _ in range(N):
    L.append(int(input()))

# Find duplicates using a set
seen = set()
duplicates = set()

for num in L:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

# Print duplicates if found
if duplicates:
    print("Duplicate numbers:", list(duplicates))
else:
    print("No duplicates found.")


# 5. Write a program to create an array of natural numbers till 20 and print it.

# Create an array of natural numbers till 20
natural_numbers = list(range(1, 21))

# Print the array
print("Array of natural numbers till 20:", natural_numbers)



# 6. Write a program to take N numbers from the user and print the frequency of every number.

# Take the number of elements from the user
N = int(input("Enter the number of elements: "))

# Take N numbers as input from the user
L = []
print(f"Enter {N} numbers:")
for _ in range(N):
    L.append(int(input()))

# Create a dictionary to store frequency
frequency = {}

# Count occurrences of each number
for num in L:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Print the frequency of each number
print("\nFrequency of each number:")
for key, value in frequency.items():
    print(f"{key}: {value}")


# 7.  Array ek tarah ka data structure hai jo ek saath multiple cheezein 
# (jaise numbers ya words) store karne ka kaam karta hai. 
# Socho, ek row hai jisme har box mein ek cheez rakhi hoti hai. 
# Tum har item ko uski position se access kar sakte ho.

# Example:

# Array = [1, 2, 3, 4, 5]

# print(Array[0])
# print(Array[1])


# 1. 
def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0  
    merged = [] 
    
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]: 
            merged.append(arr1[i])
            i += 1
        else:  
            merged.append(arr2[j])
            j += 1
    
   
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
   
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged


arr1 = list(map(int, input("Enter first sorted array: ").split()))
arr2 = list(map(int, input("Enter second sorted array: ").split()))


result = merge_sorted_arrays(arr1, arr2)
print("Merged Sorted Array:", result)


# 8. Write a program to print the sum of all the odd numbers and even numbers in the given array.
# Note: In the output, you should print odd numbers sum and even numbers sum in this order only.


# Define the array
L = [23, 45, 32, 25, 46, 33, 71, 90]

# Initialize sums for odd and even numbers
odd_sum = 0
even_sum = 0

# Loop through the array and classify numbers as odd or even
for num in L:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Print the sums (odd sum first, then even sum)
print("Sum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)


# 9. Write a program to take value N from the user and print the following pattern based on the user input.
# array = [2, 3, 5, 2, 1]
# >>


# Define the array
array = [2, 3, 5, 2, 1]

# Take user input for N
N = int(input("Enter the value of N: "))

# Print the pattern
for num in array:
    print('*' * (num * N))  # Multiply the stars by N