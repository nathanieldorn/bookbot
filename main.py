from stats import count_words

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
    return book_contents

def main ():
    print(get_book_text("books/frankenstein.txt"))

count_words(get_book_text("books/frankenstein.txt"))
