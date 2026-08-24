#   1
#   2 3
#   4 5 6
#   7 8 9 10

def Pattern(N):
    k = 1
    for i in range(1,N + 1):
        for j in range(1,i + 1):
            print(k,end=" ")
            k = k + 1

        print()

def main():
    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__=="__main__":
    main()