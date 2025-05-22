def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_char(text):
    num_char = {}
    for char in text.lower():
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    return num_char


def sort_on(d):
    return d["num"]


def get_sorted_char_count(num_char):
    sorted_list = []
    for char in num_char:
        sorted_list.append({"char": char, "num": num_char[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list