from string import ascii_lowercase

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(input_text):
    words = input_text.split()
    return len(words)

def count_each_letter(input_text):
    input_text_lowered = input_text.lower()
    single_letters = list(input_text_lowered)
    
    
    letters = {}
    for letter in single_letters:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters
    