"""Simple performance test comparing execution time of a tight loop."""

import time


def main() -> None:
    """Суммирует 1..9_999_999 и выводит сумму и время выполнения."""
    start_time = time.time()
    total = 0
    for i in range(1, 10_000_000):
        total += i
    end_time = time.time()

    print("Result:", total)
    print("Execution time:", end_time - start_time, "seconds")


if __name__ == "__main__":
    main()
