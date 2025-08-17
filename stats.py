def count_words(text):
    word_list = text.split()
    return len(word_list)


def count_characters(text):
    char_dict = dict()

    for char in text:
        char = char.lower()
        if (char in char_dict.keys()):
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_char_dict(char_dict):
    dict_list = list()

    for key in char_dict:
        if (key.isalpha() == False):
            continue;
    
        sorted_dict = dict()
        sorted_dict["char"] = key
        sorted_dict["num"] = char_dict[key]

        dict_list.append(sorted_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(element):
    return element["num"]