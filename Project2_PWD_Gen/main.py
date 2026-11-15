import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator!")
num_letters = int(input("How many letters would you like? "))
num_numbers = int(input("How many numbers would you like? "))
num_symbols = int(input("How many symbols would you like? "))

password_list = []
password = ""

for letter in range(num_letters):
    password_list.append(random.choice(letters))

for number in range(num_numbers):
    password_list.append(random.choice(numbers))

for symbol in range(num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for char in password_list:
    password += char

print(password)