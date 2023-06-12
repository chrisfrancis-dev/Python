#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(len(symbols))
print("Welcome to the Password Generator")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
let = 0
sym = 0
num = 0
password = []
total_length = nr_letters + nr_numbers + nr_symbols

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for n in range(0,nr_letters):
#   password = password + letters[random.randint(0,51)]
# for n in range(0,nr_letters):
#   password = password + numbers[random.randint(0,9)]
# for n in range(0,nr_letters):
#   password = password + symbols[random.randint(0,8)]
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for n in range(0,nr_letters):
    password.append(letters[random.randint(0,51)])
for n in range(0,nr_numbers):
    password.append(numbers[random.randint(0,9)])
for n in range(0,nr_symbols):
    password.append(symbols[random.randint(0,8)])


new_password = ""
l = len(password)
for n in range(0, l):
    p = random.choice(password)
    password.remove(p)
    new_password = new_password + str(p)


print(new_password)