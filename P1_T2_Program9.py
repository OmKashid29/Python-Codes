# Convert minutes into hours and minutes.

def Calculate(T):
    return T // 60 , T % 60

def main():
    Min = int(input("Enter the minutes : "))

    Hours , Minutes = Calculate(Min)

    print(f"{Min} Minutes is {Hours} and {Minutes} Minutes")

if __name__=="__main__":
    main()