import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit ")
    user_input.lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        print("please enter correct value ")
        continue
    
    random_number = random.randint(0,2)
     #rock:0 paper:1 scissor:2
    computer_pick = options[random_number]
    print("computer picked",computer_pick+".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_wins +=1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins +=1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins +=1
    
    else:
        print("you loose")
        computer_wins += 1
        continue

    
print("you won",user_wins,"times")  
print("computer wins",computer_wins,"times")