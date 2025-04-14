import random
while True:
    question = input("Roll a die? y/n: ").lower()
    if question == 'y' :
        try :
            numDice = int(input("How many die: "))
        except :
            print("Invalid number, try again.")
            continue
        else :
            print(f"Rolling {numDice} dice...")
            [print(f"Die Number {_ + 1 }: {x}",random.randint(1, 6))  for _,x in enumerate(range(numDice))]
              
    elif question == 'n' :
        print ('thank you for playing')
        break

    
