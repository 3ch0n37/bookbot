#! /usr/bin/env python3
from stats import count_words, count_characters

def get_book_text (path):
    with open(path) as f:
        return f.read()
    
def main ():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    character_count = count_characters(book_text)
    print(f"{num_words} words found in the document")
    print(character_count)

main()