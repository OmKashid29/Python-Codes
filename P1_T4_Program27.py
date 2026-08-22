#   *****
#   ****
#   ***
#   **
#   *

def Pattern(N):
    for i in range(N):
        print((N - i) * "*")

def main():
    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__=="__main__":
    main()