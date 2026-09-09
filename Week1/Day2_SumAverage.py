def calculate_sum(numbers: list[float]) -> float:
    total = 0.0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return calculate_sum(numbers) / len(numbers)


def main():
    nums = [15, 23, 8, 42, 16, 4]

    total = calculate_sum(nums)
    avg = calculate_average(nums)

    print(f"List: {nums}")
    print(f"Sum: {total}")
    print(f"Average: {avg:.2f}")


if __name__ == "__main__":
    main()