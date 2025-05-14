from stats import *
import sys

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count = word_count(text)
    characters = char_count(text)
    fresh_list=[]
    for x in characters:
        fresh_list = fresh_list + [{"key":x,"num":characters[x]}]
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()
    fresh_list.sort(reverse=True, key=sort_on)
    for sub in fresh_list:
        for y in sub:
            if sub["key"].isalpha() and ("key" in y):
#                print(f"The '{sub["key"]}' character was found {sub["num"]} times")
                print(f"{sub["key"]}: {sub["num"]}")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_count(full_text_in):
    char_list = {}
    new_ind_char = []
    ind_words = full_text_in.split()
    for a in ind_words:
        lower_a = a.lower()
        ind_char = list(lower_a)
        new_ind_char = new_ind_char + ind_char
    for b in new_ind_char:
        if b in char_list:
            char_list[b] += 1
        else:
            char_list[b] = 1
    return char_list

def sort_on(dict):
    return dict["num"]

main()