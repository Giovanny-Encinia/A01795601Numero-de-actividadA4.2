"""This module is for count the frequency of words in a file."""

import sys
import time


def count_words(filename: str) -> dict:
    """Counts the frequency of each distinct word in the given file."""
    word_counts: dict[str, int] = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                words: list[str] = line.strip().split()
                for word in words:
                    clean_word: str = "".join(
                        char.lower() for char in word if char.isalnum()
                    )  # Remove punctuation
                    if clean_word:
                        word_counts[clean_word] = (
                            word_counts.get(clean_word, 0) + 1
                        )  # Optimized word count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Ensure the file path is correct.")
        return None

    return word_counts


def write_results(word_counts: dict[str, int], elapsed_time: float) -> None:
    """Writes the word frequency results to a file."""
    output_filename: str = "WordCountResults.txt"
    try:
        with open(output_filename, "w", encoding="utf-8") as result_file:
            for word, count in sorted(word_counts.items()):
                result_file.write(f"{word}: {count}\n")
            result_file.write(f"Execution Time: {elapsed_time:.4f} seconds\n")
    except FileNotFoundError:
        print(f"Error: Output file '{output_filename}' not found.")


def main() -> None:
    """Main function to handle command-line execution."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <fileWithData.txt>")
        return

    filename: str = sys.argv[1]
    start_time: float = time.time()
    word_counts: dict[str, int] = count_words(filename)
    if word_counts is None:
        return

    elapsed_time: float = time.time() - start_time

    print("Word Frequency Count:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")

    write_results(word_counts, elapsed_time)
    print("Results saved to WordCountResults.txt")


if __name__ == "__main__":
    main()
