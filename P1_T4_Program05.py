# Print the multiplication table of a number.

def main():
    N = int(input("Enter the number : "))

    for i in range(N,(N*10+1),N):
        print(i)

if __name__=="__main__":
    main()