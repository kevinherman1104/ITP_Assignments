lword =  ["mantap","lol"]
def find_longest_word(lword):
    longest_length = 0
    for elements in lword:
        if len(elements) > longest_length:
            longest_length = len(elements)
    return longest_length


print(find_longest_word(lword))