def analyze_sentence(sentence: str):
    words = sentence.split()
    total_words = len(words)

    print(f"\nTotal Words: {total_words}")
    print("Word Lengths:")
    for word in words:
        clean_word = word.strip(".,!?;:\"'")
        print(f" - {clean_word}: {len(clean_word)} characters")


def main():
    sentence = input("Enter a sentence: ")
    analyze_sentence(sentence)


if __name__ == "__main__":
    main()