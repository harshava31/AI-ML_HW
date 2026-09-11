import math


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def main():
    test_numbers = [2, 11, 15, 29, 1, -5, 100]

    for num in test_numbers:
        status = "Prime" if is_prime(num) else "Not Prime"
        print(f"{num:3d} -> {status}")


if __name__ == "__main__":
    main()