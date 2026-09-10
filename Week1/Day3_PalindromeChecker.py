def is_palindrome(word: str) -> bool:
    cleaned = word.lower()
    reversed_word = ""

    # Reversing text manually using a loop
    for char in cleaned:
        reversed_word = char + reversed_word

    return cleaned == reversed_word


def main():
    word = input("Enter a word: ")

    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is NOT a palindrome.")


if __name__ == "__main__":
    main()