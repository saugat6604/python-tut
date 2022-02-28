print("Welcome to my latest quiz game")

playing = input("DO you want to play? ")

if playing != "yes":
    quit()
print("welcome to final game bro")

score=0
answer = input("what is capital of nepal? ")
if answer == "kathmandu":
    print("good man")
    score = score+1
else:print("oops incorrect")


answer = input("what is capital of india ")
if answer == "newdelhi":
    print("good man")
    score=score+1
else:
    print("oops incorrect")

answer = input("what is capital of afganistan ")
if answer == "kabul":
    print("good man")
    score += 1 
else:
    print("oops incorrect")

print("you got "+str(score)+" correct")
#print("final score "+str(score))
