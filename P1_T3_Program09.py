# Check whether a character is a vowel or consonant.

def Check(Ch):
    if (Ch == 'A' or Ch == 'E' or Ch == 'I' or Ch == 'O' or Ch == 'U' or
        Ch == 'a' or Ch == 'e' or Ch == 'i' or Ch == 'o' or Ch == 'u'
        ):
        return True
    return False

def main():
    Char = input("Enter the character : ")

    Ret = Check(Char)

    if Ret == True :
        print("Character is a vowel")
    else:
        print("Character is a constant")

if __name__=="__main__":
    main()