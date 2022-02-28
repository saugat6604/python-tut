name = input("Type your name ")
print("Welcome", name, "to this adventure ")

answer = input("Great you are in adventure you can go left or right?Which way u wanna go ")
answer.lower()
if answer == "left":
    answer = input("You come to the ocean ,you can type swim to swim or boat to go for boating ")

    if answer == "swim":
        print("you swam across pacific animal and enjoyed ")

    elif answer == "boat":
        print("you went for boating in the ocean ")

    else:
        print("not valid option ")
    
    print()


elif answer == "right":
    answer = input("You are now at pulchowk type goahead or back")
    
    if answer == "goahead":
        print("you are now at pulchowk")
    
    elif answer == "back":
        print("you have reached jawalakhel")
    else:
        print("invalid input")

else:
    print("not a valid option")