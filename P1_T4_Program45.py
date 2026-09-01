# Guess the Number game (user gets limited attempts).

import random

def Guess(Random,Attempt):
    while(Attempt != 0 ):
        print(f"You have {Attempt} attempts")
        Num = int(input("Guess the number from 1 to 100 : "))
        Attempt = Attempt - 1

        if(Num > Random):
            print("Too high")
            Guess(Random,Attempt)
            return
        elif(Num < Random):
            print("Too Low")
            Guess(Random,Attempt)
            return
        else:
            print("Right Guess")
            return
    return

def main():
    Random = random.randint(1,100)

    Attempt = 5

    Guess(Random,Attempt)
    

if __name__=="__main__":
    main()