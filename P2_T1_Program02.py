# Find the length of a string without using len().

def main():

    String  = input("Enter the string : ")
    Count = 0

    for i  in String:
        Count += 1

    print(f"Length of the String is : {Count}")

if __name__ == "__main__":
    main()