# Problem 1: Reversing a user string and counting vowels
def problem_1():
    text = input("Enter a string for Problem 1: ")
    reversed_text = text[::-1]
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    print(f"Reversed: {reversed_text}")
    print(f"Vowel Count: {vowel_count}\n")


# Problem 2: Filtering even numbers and calculating sum/average
def problem_2():
    numbers = [12, 7, 19, 24, 33, 40, 5, 18]
    even_numbers = [num for num in numbers if num % 2 == 0]
    total_sum = sum(even_numbers)
    avg = total_sum / len(even_numbers) if even_numbers else 0.0

    print(f"Original List: {numbers}")
    print(f"Even Numbers: {even_numbers}")
    print(f"Sum of Evens: {total_sum}")
    print(f"Average of Evens: {avg:.2f}\n")


# Problem 3: Dictionary character frequency with max key lookup
def problem_3():
    sentence = "python programming"
    freq = {}
    for char in sentence.replace(" ", ""):
        freq[char] = freq.get(char, 0) + 1

    most_frequent = max(freq, key=freq.get) if freq else None

    print(f"Sentence: '{sentence}'")
    print(f"Character Frequencies: {freq}")
    print(f"Most Frequent Character: '{most_frequent}' ({freq[most_frequent]} times)\n")


def main():
    print("=== Mini Practice Set ===")
    problem_1()
    print("------------------------")
    problem_2()
    print("------------------------")
    problem_3()


if __name__ == "__main__":
    main()