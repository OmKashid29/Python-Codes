# Find the first occurrence of a character.

def main():
    String = input("Enter a String : ")

    Ch = input("Enter a character ")
    Count = 0 

    for i in String:
        
        if (Ch != i):
            Count += 1

        else:
            print(f"The character {Ch} occured at {Count} index")
            break

    if (Count == len(String) ):
        print(f"The character {Ch} not found in the string")

if __name__ == "__main__":
    main()