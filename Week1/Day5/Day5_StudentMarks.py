def calculate_grade(average: float) -> str:
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    # Dictionary storing marks for 5 students across subjects
    student_marks = {
        "Alice": [85, 92, 88],
        "Bob": [78, 65, 72],
        "Charlie": [95, 98, 100],
        "Diana": [60, 58, 64],
        "Ethan": [88, 80, 84],
    }

    print("--- Student Performance Summary ---")
    print(f"{'Name':<10} | {'Average':<8} | {'Grade':<5}")
    print("-" * 30)

    for student, marks in student_marks.items():
        avg = sum(marks) / len(marks)
        grade = calculate_grade(avg)
        print(f"{student:<10} | {avg:<8.2f} | {grade:<5}")


if __name__ == "__main__":
    main()