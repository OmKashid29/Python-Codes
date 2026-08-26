# Print all Perfect numbers between 1 and 10000.

def Perfect():
    Perf = []

    for Num in range(1,1001):
        Sum = 0

        for i in range(1,Num):
            if (Num % i == 0):
                Sum = Sum + i

        if (Sum == Num):
            Perf.append(Num)

    return Perf

def main():
    Ret = Perfect()

    print(f"The Perfect numbers from 1 to 1000 are :\n{Ret}")

if __name__=="__main__":
    main()