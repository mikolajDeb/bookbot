
from string import ascii_lowercase

def sort_on(item):
    return list(item.values())[0]

def report(singles, num_of_words, filepath):
    #sorted_singles = sorted(singles.items(), key=sort_on, reverse=True)
    list_of_small_dicts = []
    for key, val in singles.items():
        small_dict = {"char": val, "num":key}
        list_of_small_dicts.append(small_dict)
    list_of_small_dicts.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Fount {num_of_words} total words")
    print("--------- Character Count -------")
    for items in list_of_small_dicts:
        print(f"{items['num']}: {items['char']}")
        print("\n")
    print("============ THE END ============")
