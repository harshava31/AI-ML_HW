def square(num: float) -> float:
    return num ** 2


def cube(num: float) -> float:
    return num ** 3


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def simple_interest(principal: float, rate: float, time: float) -> float:
    return (principal * rate * time) / 100


def main():
    print(f"Square of 5: {square(5)}")
    print(f"Cube of 3: {cube(3)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Simple Interest (P=1000, R=5%, T=2 yrs): {simple_interest(1000, 5, 2)}")


if __name__ == "__main__":
    main()