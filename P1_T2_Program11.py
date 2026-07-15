# Convert kilometers to meters and centimeters

def Calculate(KM):
    Meters = KM * 1000
    Centimeters = KM * 100000
    return Meters , Centimeters

def main():
    KM = float(input("Enter the KM : "))

    Meters , Centimeters = Calculate(KM)

    print(f"{KM} KM is {Meters} Meters and {Centimeters} Centimeters")

if __name__=="__main__":
    main()