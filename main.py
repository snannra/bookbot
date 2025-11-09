from stats import get_num_words, get_num_characters, sort_dict
import sys


def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_characters = sort_dict(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
