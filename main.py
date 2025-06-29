import sys
from stats import word_counter, char_counter, sort_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if(len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")

    print("----------- Word Count ----------")
    word_count = word_counter(get_book_text(path))
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    char_count = char_counter(get_book_text(path))

    char_list = sort_chars(char_count)
    for item in char_list:
        key = item["char"]
        value = item["num"]
        print(f"{key}: {value}")
    print("============= END ===============")

main()