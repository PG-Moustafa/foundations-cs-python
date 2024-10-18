
# SE - FCS - Assignment_04
# Moustafa Haydar

# import json

# def display():
#     print("\n1. Sum Tuples")
#     print("2. Export JSON")
#     print("3. Import JSON")
#     print("4. Exit")
#     print("---------------\n")

# def read_number_between(n1, n2, msg):
    
#     while True:
#         try:
#             number = int(input(msg))
#             if n1 <= number <= n2:
#                 return number
#         except:
#             print("Invalid input!")

# def sum_two_tuples(t1, t2):

#     if len(t1) != len(t2): return

#     result = []

#     for i in range(len(t1)):
#         result.append(t1[i] + t2[i])

#     return tuple(result)

# def read_list(msg):
#     list = input(msg)
#     list = ( int(digit) for digit in list.split(" ") if digit.isdigit())
#     return list

# def export_JSON(file_path, new_data):
    
#     try:
#         with open(file_path, 'r') as file:
#             previous_data = list(json.load(file))
#     except (FileNotFoundError, json.JSONDecodeError):
#         previous_data = []

#     if isinstance(previous_data, list):
#         previous_data.append(new_data)  # Append the new user data
#     else:
#         print("Error: Existing data is not a list.")
#         return

#     with open(file_path, 'w') as file:
#         json.dump(previous_data, file, indent=4)

# def import_JSON(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#         return data
#     except FileNotFoundError:
#         print("Error: The file was not found.")
#     except Exception as e:
#         print(f"An unexpected error occured: {e}")

# def get_new_data():
#     new_data = ""
#     print("Please enter data (type 'done' on a new line to finish):")
#     while True:
#         line = input()
#         if line.lower() == 'done':
#             break
#         new_data += line
#     try:
#         return json.loads(new_data)  # Attempt to parse the input as JSON
#     except json.JSONDecodeError:
#         print("Invalid JSON input.")
#         return {}
    
# def manage_choice(n):

#     if n == 1:
#         # return a sum tuple of two tuples

#         t1 = tuple(read_list("\nEnter a list of numbers: "))
#         t2 = tuple(read_list("Enter a list of numbers: "))

#         if len(t1) == len(t2):
#             print("\nSum of two tuples: ", sum_two_tuples(t1, t2))
#             return
            
#         print("\nLength of the tuples should be the same!")
#         manage_choice(1)

#     elif n == 2:
#         file_path = input("Please enter file path: ")
        
#         # read new dict data
#         print("Please enter data: ")
#         new_data = get_new_data()
#         export_JSON(file_path, new_data)

#     elif n == 3:

#         file_path = input("Please enter file path: ")
#         data = import_JSON(file_path)
        
#         for user in data:
#             print("\n", user)

# def start():

#     while True:
#         display()
#         choice = read_number_between(1, 4, "Enter a choice: ")
        
#         if choice == 4: 
#             print("Exit program.")
#             return
        
#         manage_choice(choice)

# start()



# # Exercise 2: 

# # Use the big-O notation to indicate the order of growth of each of the following functions
# # where N is the size of the input.

# # a. 1/6N+8000N3+24 -> O(N^3)

# # b. 1/6N3 -> O(N^3)

# # c. 1/6N! +200N4 -> O(N!)

# # d. NlogN +1000 -> O(NlogN)

# # e. logN +N -> O(N)

# # f. 1⁄2N(N-1) -> O(N^2)

# # g. N2+220NlogN2+3N+9000 -> O(N^2)

# # h. N!+3N+2N+N3+N2 -> O(N!)


##########################################################################################################