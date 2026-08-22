#   A
#   AB
#   ABC
#   ABCD
#   ABCDE

def Pattern(N):
    for i in range(1,N + 1):
        for j in range(65,65 + i ):
            print(chr(j),end="")

        print("")

def main():
    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__=="__main__":
    main()