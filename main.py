from stats import get_book_text, count_words, count_each_letter
from report import report
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Stop the program early
        
    filepath = f"{sys.argv[1]}"
    text = get_book_text(filepath)
    print (text)

    num_of_words = count_words(text)
    print(f"Found {num_of_words} total words")
    
    singles = count_each_letter(text)
    print(singles)

    report(singles, num_of_words, filepath)
 

main()