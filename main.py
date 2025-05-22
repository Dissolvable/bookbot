from stats import get_num_words, get_num_char, get_sorted_char_count
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)


def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    num_chars = get_num_char(text)
    sorted_char_count = get_sorted_char_count(num_chars)
    print_report(path, num_words, sorted_char_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(path, num_words, sorted_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()