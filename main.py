from stats import words_counter  
from stats import character_counter
from stats import sorted_list_of_dictionaries
from stats import print_sorted_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def text():
    return get_book_text(sys.argv[1])

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print (words_counter(text()))
    print("--------- Character Count -------")
    print_sorted_dictionary(sorted_list_of_dictionaries(character_counter(text())))
    print("============= END ===============")
    pass

if len(sys.argv) ==1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print(main())