# Reverse every word in a sentence.

def main():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    Reverse = "" 

    Rword = ""

    for word in words:
        for i in word:
            Rword = i + Rword

        Reverse = Reverse + Rword + " "
        Rword = ""

    print(f"After Reversing every word in a sentence : {Reverse}")
    
if __name__ == "__main__":
    main()