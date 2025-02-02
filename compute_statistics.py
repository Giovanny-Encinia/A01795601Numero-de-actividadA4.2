"""This module is for compute statistics from a file with numbers."""

import sys
import time
import logging

logger = logging.getLogger("stats_logger")
logging.basicConfig()
logger.setLevel(logging.INFO)


def open_and_read_file(filename: str, numbers: list, errors: list) -> tuple[list, list]:
    """Open the file and read the numbers and errors."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                errors.append(line.strip())
    return numbers, errors


def read_numbers_from_file(filename: str) -> tuple[list, list]:
    """Read the numbers from the file."""
    numbers = []
    errors = []
    try:
        numbers, errors = open_and_read_file(filename, numbers, errors)
    except FileNotFoundError:
        logger.warning("Error: File '%s' not found.", filename)
        sys.exit(1)
    return numbers, errors


def mean(numbers: list) -> float:
    """Calculate the mean of the numbers."""
    return sum(numbers) / len(numbers)


def variance(numbers: list, mean_: float) -> float:
    """Calculate the variance of the numbers."""
    total = 0
    for num in numbers:
        total += (num - mean_) ** 2
    return total / len(numbers)


def std_variance(variance_: float) -> float:
    """Calculate the standard deviation of the variance."""
    return variance_**0.5


def median(numbers: list) -> float:
    """Calculate the median of the numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def mode(numbers: list) -> list:
    """Calculate the mode of the numbers."""
    freq_dict = {}
    for num in numbers:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_count = max(freq_dict.values())
    mode_ = [num for num, count in freq_dict.items() if count == max_count]
    return mode_


def write_results_to_file(results: str, errors: list, execution_time: float) -> None:
    """Write the results to a file."""
    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        file.write(results)
        if errors:
            file.write("\nDatos no validos:\n")
            file.write("\n".join(errors) + "\n")
        file.write(f"Tiempo de ejecucion: {execution_time:.6f} segundos\n")


def main():
    """Main function to compute statistics from a file."""
    if len(sys.argv) != 2:
        logger.info("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers, errors = read_numbers_from_file(filename)

    if not numbers:
        logger.info("Error: No valid numbers found in the file.")
        sys.exit(1)

    mean_ = mean(numbers)
    median_ = median(numbers)
    mode_ = mode(numbers)
    variance_ = variance(numbers, mean_)
    std_dev_ = std_variance(variance_)
    execution_time = time.time() - start_time

    results = (
        f"Mean: {mean_}\n"
        f"Median: {median_}\n"
        f"Mode: {mode_}\n"
        f"Variance: {variance_}\n"
        f"Standard Deviation: {std_dev_}\n"
    )

    logger.info("Results:\n%s", results)
    logger.info("Execution time: %.3f seconds", execution_time)

    write_results_to_file(results, errors, execution_time)


if __name__ == "__main__":
    logger.info("This module is for compute statistics from a file.")
    main()
