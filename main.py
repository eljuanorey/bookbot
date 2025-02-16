
path_to_file = 'books/frankenstein.txt'
file_contents = ''
alfa_dict = {char: None for char in "abcdefghijklmnopqrstuvwxyz"}

with open(path_to_file) as f:
    file_contents = f.read()

words = file_contents.split()


def counting_words(prep_file):
    return (len(prep_file))

def counting_characters():
    lower_contents = file_contents.lower()
    count_dic = {}

    for char in lower_contents:
        if char in count_dic:
            pass
        elif char in alfa_dict:
            count_dic.update({char:lower_contents.count(char)})
    
    return count_dic

def sort_key(item):
    return item[1]

def report(char_count):
    char_dic = char_count
    char_dic_sorted = sorted(char_dic.items(),reverse=True, key=sort_key)

    for item in char_dic_sorted:
        for case in item:
            if case in alfa_dict:
                print("'" + str(case) + "'")
            else:
                print(case)

char_count = counting_characters()
report(char_count)