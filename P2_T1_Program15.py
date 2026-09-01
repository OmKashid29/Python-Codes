# Convert a string to lowercase without using .upper().

def main():

    String  = input("Enter the string : ")
    Result = ""

    for i in String:
        if ("A" <= i <= "Z"):
            Result += chr(ord(i) + 32)
        
        else :
            Result += i   

    print(f"The LowerCase String is : {Result}")

if __name__ == "__main__":
    main()