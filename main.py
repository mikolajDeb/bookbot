def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(input_text):
    words = input_text.split()
    return len(words)

def main():
    text = get_book_text("/home/mikolaj/workspace/github.com/MD/bookbot/books/frankenstein.txt")
    print (text)
    print(f"Found {count_words(text)} total words")

main()