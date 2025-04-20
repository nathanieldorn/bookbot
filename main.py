from stats import count_words, sort_counts
import sys

def select_book():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    global book_path
    book_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
    return book_contents

def print_book ():
    print(get_book_text(book_path))

def main():
    select_book()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    count_words(get_book_text(book_path))
    print("--------- Character Count -------")
    sort_counts(get_book_text(book_path))
    print("============= END ===============")

main()
