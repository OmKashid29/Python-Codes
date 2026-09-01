# Print a string in reverse.

def main():
    String = input("Enter the String : ")

    Length = len(String)

    for i in range(Length - 1,-1 ,-1):
        print(String[i], end = "")

if __name__ == "__main__":
    main()