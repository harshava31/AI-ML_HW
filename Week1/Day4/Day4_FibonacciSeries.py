def generate_fibonacci(n: int) -> list[int]:
    # Handle non-positive input edge cases
    if n <= 0:
        return []
    # Base case for a single term
    if n == 1:
        return [0]

    # Initialize the series with the first two Fibonacci numbers
    series = [0, 1]

    # Use a loop to calculate each subsequent number as the sum of the previous two
    for _ in range(2, n):
        next_val = series[-1] + series[-2]
        series.append(next_val)

    return series


def main():
    terms = 10
    fib_series = generate_fibonacci(terms)
    print(f"Fibonacci series for {terms} terms:")
    print(fib_series)


if __name__ == "__main__":
    main()