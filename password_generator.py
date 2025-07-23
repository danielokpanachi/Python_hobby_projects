import random
from random import randrange

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


for char in range(0, nr_letters):
    # random.shuffle(letters)
    password += random.choice(letters)
# print(password)

for char in range(0, nr_numbers):
    # random.shuffle(letters)
    password += random.choice(numbers)
# print(password)

for char in range(0, nr_symbols):
    # random.shuffle(letters)
    password += random.choice(symbols)
# print(password)


password_list = list(password)
random.shuffle(password_list)
shuffled_password = "".join(password_list)
print(f"Your password is: {shuffled_password}")
