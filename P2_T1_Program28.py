# Find the longest word in a sentence.

def main():
        sentence = input("Enter a sentence: ")
    
        words = sentence.split()
    
        Longest = words[0]
    
        for word in words:
            if len(word) > len(Longest):
                Longest = word
    
        print("Shortest word:", Longest)

if __name__ == "__main__":
    main()