from stats import word_count
from stats import char_count
from stats import sort_chars
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

    
def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    number_of_words = word_count(book_text)
    letter_count = char_count(book_text) 
    sorted_characters = sort_chars(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print (f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    
    for char_data in sorted_characters:
    
        character = char_data["char"]
        count = char_data["num"]
    
        if character.isalpha():
            print(f"{character}: {count}") 
    print("============= END ===============")

main()  
