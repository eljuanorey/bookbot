from stats import counting_characters, counting_words
import sys

path_to_file = sys.argv[1]
file_contents = ''
alfa_dict = {char: None for char in "abcdefghijklmnopqrstuvwxyz"}

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

with open(path_to_file) as f:
    file_contents = f.read()

words = file_contents.split()

def sort_key(item):
    return item[1]

def report(char_count):
    char_dic = char_count
    char_dic_sorted = sorted(char_dic.items(),reverse=True, key=sort_key)

    for item in char_dic_sorted:
        print(item[0] + ': ' + str(item[1]))

char_count = counting_characters(file_contents, alfa_dict)
report(char_count)