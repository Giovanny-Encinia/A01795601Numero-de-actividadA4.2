"""This module is for convert numbers to binary and hexadecimal."""

import sys
import time
from typing import List


def to_binary(n: int) -> str:
    """Converts the given integer to a binary string."""
    return "0" if n == 0 else bin(n)[2:]


def to_hexadecimal(n: int) -> str:
    """Converts the given integer to a hexadecimal string."""
    return "0" if n == 0 else hex(n)[2:].upper()


def process_file(filename: str) -> None:
    """Reads a file with numbers and converts them to binary and hexadecimal."""
    start_time = time.time()
    results: List[str] = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    for line in lines:
        try:
            number = int(line.strip())
            binary = to_binary(number)
            hexadecimal = to_hexadecimal(number)
            results.append(f"{number}: Binary={binary}, Hexadecimal={hexadecimal}")
        except ValueError:
            print(f"Invalid data: '{line}' is not a valid number. Skipping...")

    elapsed_time = time.time() - start_time
    results.append(f"Execution Time: {elapsed_time:.4f} seconds")

    # Print results to console and save to file
    result_text = "\n".join(results)
    print(result_text)

    with open("ConvertionResults.txt", "w", encoding="utf-8") as output_file:
        output_file.write(result_text)

    print("Results saved to ConvertionResults.txt")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
    else:
        process_file(sys.argv[1])
