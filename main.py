import sys

from stats import count_words
from stats import count_characters
from stats import sort_char_dict

def get_book_text(file_path):
    
    contents = ""
    with open(file_path) as file:
        contents = file.read()

    return contents

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    contents = get_book_text(book_path)
    word_count = count_words(contents)
    char_dict = count_characters(contents)
    sorted_list = sort_char_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for element in sorted_list:
        print(f"{element["char"]}: {element["num"]}")

main()