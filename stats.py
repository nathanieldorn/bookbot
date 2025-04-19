def count_words(book_contents):
    num_words = len(book_contents.split())
    print(f"Found {num_words} total words")

def count_char(book_contents):
    book_chars = {}
    for char in book_contents.lower():
        if char in book_chars:
            book_chars[char] += 1
        else:
            book_chars[char] = 1
    for char in book_chars:
        print(f"'{char}': {book_chars[char]}")

def sort_counts(book_contents):
    book_chars = {}
    for char in book_contents.lower():
        if char in book_chars:
            book_chars[char] += 1
        else:
            book_chars[char] = 1
    sorted_book_chars = dict(sorted(book_chars.items(), key=lambda item: item[1], reverse=True))
    for char in sorted_book_chars:
        if char.isalpha():
            print(f"{char}: {sorted_book_chars[char]}")
