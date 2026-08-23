#    *********
#     *******
#      *****
#       ***
#        *

def Pattern(N):
    for i in range(N,0,-1):
        print(" " * (N - i) ,"*" * (i * 2 - 1))

def main():
    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__=="__main__":
    main()