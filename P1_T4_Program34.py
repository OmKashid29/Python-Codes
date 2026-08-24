#   *
#   **
#   ***
#   ****
#   *****
#   ****
#   ***
#   **
#   *

def Pattern(N):
    for i in range(1,N + 1):
        print(i * "*")

    for i in range(N - 1,0 ,-1):
        print(i * "*")

def main():
    Num = int(input("Enter the number : "))

    Pattern(Num)

if __name__=="__main__":
    main()