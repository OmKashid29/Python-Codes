# Replace all spaces with -.

def main():
    String = input("Enter a String : ")

    Result = ""

    for i in String:
        if (i != " "):
            Result += i
        else:
            Result += "-"

    print(f"String after replacing spaces with - is : {Result}")

if __name__ == "__main__":
    main()