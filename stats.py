def count_words():
    book_contents = get_book_text("books/frankenstein.txt")
    num_words = len(book_contents.split())
    print(f"{num_words} words found in the document")

count_words()
