from stats import get_book_text, count_words, count_each_letter

def main():
    text = get_book_text("/home/mikolaj/workspace/github.com/MD/bookbot/books/frankenstein.txt")
    print (text)
    print(f"Found {count_words(text)} total words")
    
    singles = count_each_letter(text)
    print(singles)


main()