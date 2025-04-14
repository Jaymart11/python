import random

randomNumber = random.randint(1, 100);

while True:
    try :
        guess = int(input("Guess the number between 1 to 100: "))
        if(guess > 100):
            print("only number from 1 - 100")
            continue
    except : 
        print("Invalid guess only use numbers")
    else : 
        if(guess > randomNumber):
            print("high")
        elif(guess < randomNumber):
            print("low")
        else:
            print("Correct")
            break
