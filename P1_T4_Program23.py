# Calculate the product of digits.

def Calculate(Num):
    Product = 1

    while(Num > 0):
        Rem = Num % 10
        Num = Num // 10
        Product = Product * Rem

    return Product

def main():
    Num = int(input("Enter the number : "))

    Ret = Calculate(Num)

    print(f"The Product of the digits of number {Num} is {Ret}")

if __name__=="__main__":
    main()