#   1
#   22
#   333
#   4444
#   55555

def Pattern(N):
    for i in range(1,N + 1):
        for j in range(1,i + 1):
            print(i,end="")

        print("")

def main():
    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__=="__main__":
    main()