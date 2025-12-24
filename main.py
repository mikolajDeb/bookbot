from stats import get_book_text, count_words, count_each_letter
from report import report

def main():
    filepath = "/home/mikolaj/workspace/github.com/MD/bookbot/books/frankenstein.txt"
    text = get_book_text(filepath)
    print (text)

    num_of_words = count_words(text)
    print(f"Found {num_of_words} total words")
    
    singles = count_each_letter(text)
    print(singles)

    report(singles, num_of_words, filepath)

    

main()