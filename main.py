#! /usr/bin/env python3
from stats import count_words, count_characters, generate_report

def get_book_text (path):
    with open(path) as f:
        return f.read()
    
def main ():
    book_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    character_count = count_characters(book_text)
    report = generate_report(character_count)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for line in report:
        print(f"{line["character"]}: {line["count"]}")
    print("============= END ===============")

main()