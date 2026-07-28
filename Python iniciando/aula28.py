name = input("What is your name:")
age = input("What is your age(ex: 25):")

if name and age.isdigit():
    print(f"Your name is {name} and you are {age} years old.")
    print(f"Your inverted name is {name[::-1]} and your age in 10 years will be {int(age) + 10}.")
    print(f"Your name have spaces: {'Yes' if ' ' in name else 'No'}")
    print(f"Your name have {len(name)} characters.")
else:
    print("You must fill both fields.")