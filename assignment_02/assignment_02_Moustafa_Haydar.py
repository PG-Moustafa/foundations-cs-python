
# FCS-58-MoustafaHaydar
# Instructor: Johnny Attieh
# Assignment-2

#-------------------------------------------------------------

# Exercise 1

# def calculateFactorial(n):
#     # Special case for n == 0 and n == 1
#     if n == 0 or n == 1:
#         print(1)
#         return

#     if n < 0:
#       return
    
#     factorial = 1
#     numbers = []

#     for i in range(1, n+1):
#         numbers.append(i)
#         factorial *= i

#     print(factorial, "(", end="")
#     for i in range(1, len(numbers)+1):
#         print(i, end="")
#         if i != len(numbers):
#             print(" * ", end="")
#     print(")")

# x = int(input("Enter a number to calculate factorial: "))
# calculateFactorial(x)

#------------------------------------------------------------------

# Exercise 2

# note: the output of Example 3 should not be an empty list
# every integer has at least one divisor: 1 and the number itself.
# For the input 5, the correct output should be [1, 5], not [].


# def find_divisors(n):
#     if n == 0:
#         print("Divisors of 0 are undefined.")
#         return
    
#     # check divisors for the absolute value of n
#     divisors = []
#     for i in range(1, abs(n)+1):
#         if abs(n) % i == 0:
#             divisors.append(i)
    
#     # print divisors
#     print(f"Divisors of {n}: [", end="")
#     for i in range(len(divisors)):
#         print(divisors[i], end="")
#         if i != len(divisors)-1:  # print ", " if not last case
#             print(", ", end="")
#     print("]")

# x = int(input("Enter a number to find divisors: "))
# find_divisors(x)

#-----------------------------------------------------------------

# Exercise 3

# Solution 1

# def reverseString(s):
#   return x[::-1]

# Solution 2

# def reverseString(s):
#     str = []
#     i = len(s) -1
#     while i >= 0:
#         str += s[i]
#         i -= 1
#     return ''.join(str)

# str = input("Enter a string to reverse: ")
# print(reverseString(str))

#-------------------------------------------------------------------

# Exercise 4

# def checkEvens(nums):
#     evens = []
#     for i in nums:
#         if i % 2 == 0:
#             evens.append(i)
#     return evens

# nums = input("Enter a list of numbers (,): ")
# nums = [int(num) for num in nums.split(",")]
# print(checkEvens(nums))

#-------------------------------------------------------------------

# Exercise 5

# def checkStrongPassword(password):
#     specials = ['#', '?', '!', '$']

#     contains_lower = any(char.islower() for char in password)
#     contains_upper = any(char.isupper() for char in password)
#     contains_digit = any(char.isdigit() for char in password)
#     contains_special = any(char in specials for char in password)
    
#     if len(password) >= 8 and contains_digit and contains_lower and contains_special and contains_upper:
#         print("Strong password")
#     else:
#         print("Weak password")

# password = input("Enter your password to check it: ")
# checkStrongPassword(password)

#-------------------------------------------------------------------

# Exercise 6

# def checkIPv4(ip):
#     numbers = ip.split('.')

#     if len(numbers) != 4:
#         return False

#     for n in numbers:
        
#         if not n.isdigit():
#             return False

#         if n != '0' and n.startswith('0'): #0 #012
#             return False

#         if not (0 <= int(n) <= 255):
#             return False
        
#     return True

# x = input("Enter an IPv4: ")
# print(checkIPv4(x))


#---------------------------------------------------------------------
