
# FCS CYCLE 58
# Assignment_3
# Moustafa Haydar

# def print_menu():
#     print("\n1. Count Digits")
#     print("2. Find Max")
#     print("3. Count Tags")
#     print("4. Exit")
#     print("-----------------")

# def read_number_between(n1, n2, message):
#     choice = -1

#     while (not (n1 <= choice <= n2)):
#         choice = int(input(message))

#         if (not (n1 <= choice <= n2)):
#             print("Choice out of range!")

#     return choice

# def count_digits(num):
#     num = abs(num)

#     if num == 0:
#         return 0

#     # count digits using Recursion
#     return 1 + count_digits(num//10)

# def find_max(items):

#     if len(items) == 0:
#         return 0

#     elif len(items) == 1:
#         return items[0]

#     else:
#         max = items[0]
#         for item in items:
#             if item > max:
#                 max = item

#     return max
    
# def read_list_nums():
#     items = input("\nEnter a list of numbers (comma-separated): ")
    
#     if items: # check if the input non empty string
#         items = [int(item) for item in items.split(",")]

#     return items

# def count_tags(html, tag, index = 0, count = 0):

#     # Opening and closing tags
#     opening_tag = f"<{tag}>"
#     closing_tag = f"</{tag}>"

#     if index >= len(html):
#         return count

#     if html[index : index + len(opening_tag)] == opening_tag:
#         count += 1
#         index += len(opening_tag)

#     elif html[index : index + len(closing_tag)] == closing_tag:
#         index += len(closing_tag)

#     else: 
#         index += 1

#     return count_tags(html, tag, index, count)

# def manage_user_option(choice):

#     if choice == 1:

#         # 1. Count Digits
#         while True:
#             n1 = input("\nEnter a number: ")
#             if n1.lstrip('-').isdigit():
#                 n1 = int(n1)
#                 print("Count of digits = ", end="")
#                 print(count_digits(n1))
#                 break
#             else:
#                 print("Please enter a valid number.")
#                 manage_user_option(1)

#     elif choice == 2:

#         #2. Find Max
#         nums = read_list_nums()
#         print("Max of the list = ", end = "")
#         print(find_max(nums))
    
#     elif choice == 3:

#         #3. Count Tags
#         print("Enter multiple lines of input (Press Enter twice to stop): ")

#         html = ""
#         while True:
#             line = input()
#             if line == "": 
#                 break
#             html += line

#         tag = input("Enter the tag you want to count (h1, li, ...): ")

#         occurences = count_tags(html, tag)
#         print(f"The tag {tag} occurs {occurences} time(s) in the HTML code.")

# def start():

#     while True:

#         print_menu()
#         choice = read_number_between(1, 4, "Enter a choice: ")

#         if choice == 4:
#             return

#         manage_user_option(choice)
    

# start()
