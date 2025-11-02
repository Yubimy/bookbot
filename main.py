from stats import number_of_words, letter_counts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def report(file_path,word_count, sorted_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for list_item in sorted_list:
        if list_item["char"].isalpha():
            print(f'{list_item["char"]}: {list_item["num"]}')
    print('============= END ===============')

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    word_count = number_of_words(get_book_text(file_path))
    letter_dict = letter_counts(get_book_text(file_path))
    report(file_path, word_count, letter_dict)
    
main()