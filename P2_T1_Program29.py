# Find the shortest word in a sentence.

def main():
    sentence = input("Enter a sentence: ")

    words = sentence.split()

    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    print("Shortest word:", shortest)

if __name__ == "__main__":
    main()