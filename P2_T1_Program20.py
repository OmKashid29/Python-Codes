# Find the last occurrence of a character.

def main():
    String = input("Enter a String : ")

    Ch = input("Enter a character ")
    Count = 0 
    N = 0

    for i in String:
        
        if (Ch != i):
            Count += 1

        else:
            N = Count
            Count += 1

    if (Count == len(String) and N == 0 ):
        print(f"The character {Ch} not found in the string")
    else:
        print(f"Last occurence of character found index at {N}")

if __name__ == "__main__":
    main()