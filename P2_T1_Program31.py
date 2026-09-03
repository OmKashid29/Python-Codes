# Find the frequency of every character in a string.

def main():
    String = input("enter the string : ")
    Dict = {}

    for i in String:
        if (i == " "):
            continue
        elif i in Dict:
            Dict[i] += 1
        else:
            Dict[i] = 1

    print(Dict) 

if __name__ == "__main__":
    main()