# Print all Prime numbers between 1 and 1000.

def Prime():
    Pri = []
    for Num in range(1,1001):
        Count = 0
        for i in range(1,Num + 1):
            if(Num % i == 0 ):
                Count = Count + 1
        
        if Count == 2 :
            Pri.append(Num)

    return Pri       

def main():
    Ret = Prime()

    print(f"The Prime numbers from 1 to 1000 are :\n{Ret}")

if __name__=="__main__":
    main()