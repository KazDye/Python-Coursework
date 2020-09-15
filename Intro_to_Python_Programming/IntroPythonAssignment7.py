f = open("thefrenchchampagne.txt", mode='r', encoding='utf-8-sig')
line_count, char_count, word_count = 0, 0, 0,
nospace_count, unique_words, used_count = 0, 0, 0
words, char_list, letter_list = [], [], []
result, most_used = '', ''
word_dict = {}

def addwrd_func(characters):
    result = ''
    for element in char_list:
        if element not in (' ', ':', '.',',','"'):
            result += element
        else:
            if result == '':
                continue
            else:
                words.append(result)
                result = ''
    words.append(result)
    return words

def nospc_func(characters):
    nospace_count = 0
    for blanks in char_list:
        if blanks == ' ':
            char_list.remove(blanks)
            nospace_count += 1
        else:
            nospace_count += 1
    return nospace_count

def count_func(word):
    word_count = 0
    for count in words:
        word_count += 1
    return word_count

def dic_func(word):
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

def unique_func(dictionary):
    unique_words = 0
    for word, value in word_dict.items():
        if word_dict[word] == 1:
            unique_words += 1
        else:
            continue
    return unique_words

def highest_func(dictionary):
    most_used = ''
    used_count = 0
    maxi = 0
    for word, value in word_dict.items():
        if word_dict[word] > maxi:
            maxi = word_dict[word]
            most_used = word
            used_count = value
        else:
            continue
    return most_used, used_count

for line in f:
    line = line.strip()
    line_count += 1
    print(line_count, ' - ', line)
    line = line.lower()
    for char in line:
        char_list.append(char)
        char_count += 1
words = addwrd_func(char_list)
nospace_count = nospc_func(nospace_count)
word_count = count_func(word_count)
word_dict = dic_func(word_dict)
unique_words = unique_func(word_dict)
most_used, used_count = highest_func(word_dict)

print("Number of Lines:", line_count)
print("Number of Words:", word_count)
print("Number of Characters Without Spaces:", nospace_count)
print("Number of Characters With Spaces:", char_count)
print("Number of Unique Words:", unique_words)
print("The Most Used Word Was:", most_used.title(), "Used A Whopping", used_count, "Times!")
