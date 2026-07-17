# Swap two numbers without using a third variable.

def Swap(a,b):
    a,b = b,a
    return a,b

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
    print(f"Numbers before swapping No1 = {No1} and No2 = {No2}")
    No1,No2 = Swap(No1,No2)
    print(f"Numbers after swapping No1 = {No1} and No2 = {No2}")

if __name__=="__main__":
    main()
