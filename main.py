def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents
def main():
    text = get_book_text("/home/mikolaj/workspace/github.com/MD/bookbot/books/frankenstein.txt")
    print (text)

main()