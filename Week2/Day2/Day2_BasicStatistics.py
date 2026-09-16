import numpy as np


def main():
    data = np.array([12, 15, 22, 28, 30, 45, 50, 62])

    np_mean = np.mean(data)
    np_median = np.median(data)
    np_std = np.std(data)

    manual_mean = sum(data) / len(data)
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        manual_median = sorted_data[n // 2]
    else:
        manual_median = (sorted_data[(n // 2) - 1] + sorted_data[n // 2]) / 2

    print(f"Data: {data}\n")
    print(f"NumPy Mean:   {np_mean:.2f} | Manual Mean:   {manual_mean:.2f}")
    print(f"NumPy Median: {np_median:.2f} | Manual Median: {manual_median:.2f}")
    print(f"NumPy StdDev: {np_std:.2f}")


if __name__ == "__main__":
    main()