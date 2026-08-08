# Find the sum of odd numbers up to N

def main():
    Sum = 0

    N = int(input("Enter the number : "))

    for i in range(1,N + 1,2):
        Sum = Sum + i
    
    print(f"The sum of 1 to {N} odd number is {Sum}")

if __name__=="__main__":
    main()