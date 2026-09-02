# Check whether a character exists in a string.

def main():
    String = input("Enter a String : ")

    Ch = input("Enter a character ")
    Count = 0 

    for i in String:
        if (Ch == i):
            Count += 1
            break

    if Count != 0 :
        print("Character exists in a string.")
    else:
        print("Character does not exist in a string.")

if __name__ == "__main__":
    main()