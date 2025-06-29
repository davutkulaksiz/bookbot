def word_counter(text):
    return len(text.split())

def char_counter(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    char_list = []

    for key in chars.keys():
        if(key.isalpha()):
            item = {
                "char": key,
                "num": chars[key]
            }
            char_list.append(item)
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list
    