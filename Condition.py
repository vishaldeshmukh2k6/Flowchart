# 1. Write a program to take two numbers from the user and determine the greater of those two given numbers.

# Input:
# 20
# 3

# Output:
# 20

#code :

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(num1)
else:
    print(num2)


# 2. Write a program to take a number from the user and print that number as Odd or Even.

# Test Case1:
# Input:
# 56
# Output:
# Even
# Test Case2:
# Input:
# 87
# Output:
# Odd


#code :

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Write a program to take a number from the user and output whether that number is negative, p
#    ositive or zero. 

#  Test Case1:
#  Input: 6 

# Output: 
# Positive 

#  Test Case2:
#  Input:
#  0 

# Output: 
# Zero

# code :

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 4. Write a program to take an integer as input and print the smallest positive integer that is 
#    a multiple of both 2 and n.

# Test Case:
# Input:
# 5
# Output:
# 10

# Test Case:
# Input:
# 6
# Output:
# 6

#code :

n = int(input("Enter an integer: "))

if n % 2 == 0:
    print(n)  
else:
    print(2 * n)

