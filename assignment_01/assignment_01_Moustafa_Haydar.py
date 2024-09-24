
#-----------------------------------------------

# SE FACTORY
# FCS CYCLE 58
# Assignment 1

# Instructor: Mr. Johnny Attieh
# Name: Moustafa Haydar

# -----------------------------------------------

# Exercise 1

# # Read 3 numbers from user
# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a second number: "))
# num3 = int(input("Enter a third number: "))

# # Find maximum value 
# max = num1
# if (num2 > num1 and num2 > num3) : 
#     max = num2
# elif (num3 > num2 and num3 > num1) :
#     max = num3

# print("Maximum value is ", max)

# ------------------------------------------------

# # Exercise 2

# # Input a positive number
# while True:
#         n = int(input("Enter a positive number: "))
#         if n > 0:
#             break # will exit if number is positive
#         else:
#             print("Number must be positive")

# product = 1
# while n > 0:
#     if n % 2 != 0: # check if Odd
#         product *= n
#     if product > 100:
#         print("Multiplication exceeded")
#         break
#     n -= 1

# if product <= 100:
#      print("Product = ", product)

# ------------------------------------------------

#Exercise 3
# sum = 0.0
# count = 0

# while True:
#     n = float(input("Enter a score (or -1 to stop): "))
#     if n == -1:
#         break
#     sum += n
#     count += 1


# if count > 0: # prevent division by zero
#     avg = sum / count
#     print(f"Average of the scores is : {avg:.1f}")
# else:
#     print("No scores were entered.")

# ------------------------------------------------

# Exercise 4

# num = int(input("Input a four-digit number: "))
# if 1000 <= num <= 9999:
#     A = num//1000
#     B = (num//100) %10
#     C = (num//10) %10
#     D = num %10
#     if ( A + B == C + D):
#         print("F")
#     else: print("U")
# else:
#     print("The number is not a four-digit.")

