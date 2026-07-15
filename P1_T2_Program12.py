# Convert bytes into KB, MB, and GB.

def Calculate(B):

    KB = B / 1024
    MB = KB / 1024
    GB = MB / 1024

    return KB,MB,GB   

def main():
    Bytes = int(input("Enter the Bytes : "))

    KB,MB,GB = Calculate(Bytes)
    print(f"{Bytes} bytes equal to {KB} in KB , {MB} in MB ,{GB} in GB")

if __name__=="__main__":
    main()