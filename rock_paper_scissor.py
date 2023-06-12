rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
ranval = random.randint(1,3)

user_input =int(input("Enter '1' for rock '2' for paper and '3' for scissors "))
if(user_input == 1):
  print(rock)
elif(user_input == 2):
  print(paper)
else:
  print(scissors)

if(ranval == 1):
  print(rock)
elif(ranval == 2):
  print(paper)
else:
  print(scissors)

if(ranval == user_input):
  print("It is a draw")
elif(user_input == 1 and ranval == 3 or user_input == 2 and ranval == 1 or user_input == 3 and ranval == 2):
  print("You win")
else:
  print("You lose")
