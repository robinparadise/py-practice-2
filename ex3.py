'''
Exercise rock, paper, scissors
'''

import random

# 1. Create a list of rock, paper, scissors in a variable called rps.
# "rps" means rock, paper, scissors
rps = ['rock','paper','scissors']

# 2. Create a variable called user_choice that takes input from the user and stores it.
#   Make sure the user enters rock, paper, or scissors.
user_choice = "" # fix this, user input, hint: use input("...")

# 3. Create a variable called computer_choice that randomly chooses from rps.
computer_choice = "" # fix this, random choice from rps

# 4. Print out the user_choice and the computer_choice.
print("You chose: " + user_choice)
print("The computer chose: " + computer_choice)

# 5. Print out the winner of rock, paper, scissors.
# continue this if statement to print out the winner
if user_choice == computer_choice:
  print("It's a tie!")
# write stuff here

# rock beats scissors
# paper beats rock
# scissors beats paper
# hint: use elif
# hint: use and or not == !=
# hint: use "It's a tie!"
# hint: use "You win!"
# hint: use "You lose!"

# Example of an if statement:
# math = input("What is 2 + 2? ")
# if math == "4":
#   print("You are correct!")
# elif math == "3":
#   print("You are close!")
# else:
#   print("You are wrong!")
