import random
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
print("Welcome to Rock, Paper, Scissors automated game!!!")
print("Here are the options Enter 0 for Rock, 1 for paper, 2 for scissors.")
user_choice = input("which one would you choose? Rock, Paper or Scissors.\n")
print("\n")
print("User choice:")
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("the input you entered is invalid. Please you read from the options menu.")

while user_choice == "0" or user_choice == "1" or user_choice == "2":
    print("Computer Choice:")
    computer_choice = [rock, paper, scissors]
    for i in range(1):
        computer_chosen = random.choice(computer_choice)
        print(computer_chosen)
    if(user_choice == "0" and computer_chosen == computer_choice[2]):
        print("You Win! YAY!")
        break
    elif(user_choice == "2" and computer_chosen == computer_choice[1]):
        print("You Win! YAY!")
        break
    elif(user_choice == "1" and computer_chosen == computer_choice[0]):
        print("You Win! YAY!")
        break
    elif(computer_chosen == computer_choice[0] and user_choice == "2"):
        print("You lose! Better luck next time")
        break
    elif(computer_chosen == computer_choice[1] and user_choice == "0"):
        print("You lose! Better luck next time")
        break
    elif(computer_chosen == computer_choice[2] and user_choice == "1"):
        print("You lose! Better luck next time")
        break
    elif(computer_chosen == computer_choice[0] and user_choice == "0" or computer_chosen == computer_choice[1] and user_choice == "1" or computer_chosen == computer_choice[2] and user_choice == "2"):
        print("uh oh! Its a Draw")
        break
    else:
        print("You are a bag of guavas.")
        break
