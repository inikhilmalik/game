import random
randomNo=random.randint(1,100)
#print(randomNo)

userguess=None
guesses=0

while(userguess != randomNo):
    userguess=int(input("enter your guess : "))
    guesses+=1
    if (userguess==randomNo):
        print("you guess a right number ")
    else:
        if(userguess > randomNo):
            print("you guess a wrong number . please enter a small number ")
        else:
            print("you guess a wrong number . please enter a large number ")
print(f"you guess the number in {guesses} guesses ")