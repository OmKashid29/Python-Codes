# Check whether a character is uppercase or lowercase.

def Check(C):
    if 'A' <= C and  C <= 'Z':
        print(f"{C} is uppercase character ")

    elif 'a' <= C and  C <= 'z':
        print(f"{C} is lowercase character ")

    else:
        print(f"{C} not a character")

def main():
    Char = input("Enter a character : ")

    Check(Char)

if __name__=="__main__":
    main()