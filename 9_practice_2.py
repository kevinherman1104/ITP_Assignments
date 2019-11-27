lwords = ["saya","mau","makan"]
def filter_long_words(lwords):
    list_longer_than_n = ""
    n = 4
    for element in lwords:
        if len(element) > n:
            list_longer_than_n = element
    return(list_longer_than_n)

print(filter_long_words(lwords))