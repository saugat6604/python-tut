import random

top_of_range = input("type a number for random number generation ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter number greater than 0 ")
        quit()

else:
    print("please enter a number next time")
    quit()

random_number = random.randint(0,top_of_range)
guess = 0
# print(random_number)

while True:
    guess += 1
    user_guess = input("Make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
         print("please enter a number next time")
         continue 

    if user_guess == random_number:
        print("you got it")
        #print(random_number)
        break
    
    elif user_guess > random_number:
        print("you are above")

    else:
        print("you are below")
        #print(random_number)

print("total guess "+str(guess))
        
        


    

    


    


