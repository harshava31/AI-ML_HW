def get_length(text: str) -> int:
    return len(text)


def to_uppercase(text: str) -> str:
    return text.upper()


def to_lowercase(text: str) -> str:
    return text.lower()


def reverse_string(text: str) -> str:
    return text[::-1]


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def main():
    user_text = input("Enter a string: ")

    print(f"Length: {get_length(user_text)}")
    print(f"Uppercase: {to_uppercase(user_text)}")
    print(f"Lowercase: {to_lowercase(user_text)}")
    print(f"Reversed: {reverse_string(user_text)}")
    print(f"Vowel Count: {count_vowels(user_text)}")


if __name__ == "__main__":
    main()