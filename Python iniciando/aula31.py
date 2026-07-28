## PROBLEMA 1

# number = input("Please enter a number: ")

# try:
#     number_int = int(number)
    
#     if number_int % 2 == 0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")

# except ValueError:
#     print("That's not a valid number.")





## PROBLEMA 2

# saudation = input("Please, what time is it? (HH:MM) ")
# try:
#     hours, minutes = map(int, saudation.split(":"))
    
#     if 0 <= hours < 12:
#         print("Good morning!")
#     elif 12 <= hours < 18:
#         print("Good afternoon!")
#     elif 18 <= hours <= 23:
#         print("Good evening!")
#     else:
#         print("Invalid time. Hours should be between 0 and 23.")
# except ValueError:
#     print("Invalid time format. Please use HH:MM.")







## PROBLEMA 3

# name = input("Type your name: ")

# length = len(name)

# print(f"Your name has {length} letters.")

# if length < 4:
#     print("Your name is very short!")
# elif 4 <= length <= 6:
#     print("Your name is normal!")
# else:
#     print("Your name is long!")