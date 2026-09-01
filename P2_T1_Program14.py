# Convert a string to uppercase without using .upper().

def main():

    String  = input("Enter the string : ")
    Result = ""

    for i in String:
        if ("a" <= i <= "z"):
            Result += chr(ord(i) - 32)
        
        else :
            Result += i   

    print(f"The UpperCase String is : {Result}")

if __name__ == "__main__":
    main()