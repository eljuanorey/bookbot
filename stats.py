def counting_words(prep_file):
    return (len(prep_file))

def counting_characters(file_contents, alfa_dict):
    lower_contents = file_contents.lower()
    count_dic = {}

    for char in lower_contents:
        if char in count_dic:
            pass
        elif char in alfa_dict:
            count_dic.update({char:lower_contents.count(char)})
    
    return count_dic