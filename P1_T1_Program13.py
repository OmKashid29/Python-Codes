# Calculate Area and Circumference of a Circle.

def Calculate(R):
    return R*R*3.14 , 2*3.14*R

def main():
    Radius = float(input("Enter the radius of circle : "))

    Area , Circumference = Calculate(Radius)
    print(f"Area is {Area} \nCircumference is {Circumference}")

if __name__=="__main__":
    main()