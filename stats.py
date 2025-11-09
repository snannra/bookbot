def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_dict(d):
    new_list = []
    for key in d:
        new_dict = {"char": key, "num": d[key]}
        new_list.append(new_dict)
    new_list.sort(key=lambda x: x["num"], reverse=True)
    return new_list
