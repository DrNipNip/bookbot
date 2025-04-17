import sys
from stats import *



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        text = sys.argv[1]
        content = get_num_words(text)
        num_words = len(content.split())
        num_chars = count_characters(content)
        sort_list = sort_dict(num_chars)
        
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for char in sort_list:
            if char.isalpha():
                print(f"{char}: {sort_list[char]}")

        print("============= END ===============")



main()