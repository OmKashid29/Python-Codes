# Find the sum of the first N natural numbers.

def main():
    Sum = 0

    N = int(input("Enter the number : "))

    for i in range(1,N + 1):
        Sum = Sum + i
    
    print(f"The sum of 1 to {N} is {Sum}")

if __name__=="__main__":
    main()