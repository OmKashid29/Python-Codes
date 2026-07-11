# Convert Celsius to Fahrenheit.

def Calculate(C):
    return (C * 1.8) + 32
    

def main():
   Celsius = float(input("Enter the temperature in degree Celsius : "))
   Fahrenheit = Calculate(Celsius)
   
   print(f"Temperature in Fahrenheit is {Fahrenheit}")

if __name__=="__main__":
    main()