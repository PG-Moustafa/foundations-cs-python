
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


# calculateFactorial(4)
# calculateFactorial(6)
# calculateFactorial(1)
# calculateFactorial(0)

#------------------------------------------------------------------

# Exercise 2

# note: the output of Example 3 should not be an empty list
# every integer has at least one divisor: 1 and the number itself.
# For the input 5, the correct output should be [1, 5], not [].

# def find_divisors(n):
    
#     # check divisors
#     divisors = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisors.append(i)
    
#     # print divisors
#     print("[", end="")
#     for i in range(len(divisors)):
#         print(divisors[i], end="")
#         if i != len(divisors)-1: # print ", " if not last case
#             print(", ", end="")
#     print("]")



# find_divisors(10)
# find_divisors(16)
# find_divisors(5)
# find_divisors(0)

#-----------------------------------------------------------------

# Exercise 3

# def reverseString(s):
#     str = []
#     i = len(s) -1
#     while i >= 0:
#         str += s[i]
#         i -= 1
#     return ''.join(str)

# print(reverseString("Hello World"))
# print(reverseString("oneword"))

#-------------------------------------------------------------------

# Exercise 4

# def checkEvens(nums):
#     evens = []
#     for i in nums:
#         if i % 2 == 0:
#             evens.append(i)
#     return evens

# print(checkEvens([1, 2, 3, 4, 5, 6]))
# print(checkEvens([5, 3, 18, 4, 2, 7, 10]))
# print(checkEvens([5, 3, 11, 5, 1]))

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


# checkStrongPassword("Hello5?world")
# checkStrongPassword("password")
# checkStrongPassword("Password123")
# checkStrongPassword("pAs1$!") # less than 8 char

#-------------------------------------------------------------------

# Exercise 6

# def checkIPv4(ip):
#     numbers = ip.split('.')

#     if len(numbers) != 4:
#         return False

#     for n in numbers:
        
#         if not n.isdigit():
#             return False

#         if n != '0' and n.startswith('0'):
#             return False

#         if not (0 <= int(n) <= 255):
#             return False
        
#     return True


# print(checkIPv4("256.168.1.1"))
# print(checkIPv4("192.168.1"))
# print(checkIPv4("10.0.0.01"))
# print(checkIPv4("192.168.01.1"))
# print(checkIPv4("192.168.1.1.1"))
# print(checkIPv4("192.168..1"))
# print(checkIPv4("192.168.1.-1"))

#---------------------------------------------------------------------
