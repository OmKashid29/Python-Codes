# Print all Armstrong numbers between 1 and 1000.

def Armstrong():
    Arm = []
    for Num in range(1,1001):
        
        Org = Num 
        Rev = 0
        while (Num > 0):
            Rem = Num % 10
            Num = Num // 10
            Rev = Rem ** 3 + Rev

        if (Rev == Org):
            Arm.append(Rev)
        
    return Arm

def main():
    Ret = Armstrong()

    print(f"The Armstrong numbers from 1 to 1000 are :\n{Ret}")

if __name__=="__main__":
    main()