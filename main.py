from stats import count_words, sort_counts

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

def print_book ():
    print(get_book_text("books/frankenstein.txt"))

def main():
    path_of_book = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_of_book}")
    print("----------- Word Count ----------")
    count_words(get_book_text(path_of_book))
    print("--------- Character Count -------")
    sort_counts(get_book_text(path_of_book))
    print("============= END ===============")

main()
