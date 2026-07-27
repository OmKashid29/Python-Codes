# Check whether a character is an alphabet.

def Check(Ch):
    if ('A' <= Ch <= 'Z' or 'a' <= Ch <= 'z'):
        return 'Alphabet'
    return 'Not Alphabet'

def main():
    Char = input("Enter a character : ")

    Ret = Check(Char)

    print(f"The character is {Ret}")

if __name__=="__main__":
    main()