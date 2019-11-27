word_1 = ["saya","mau","makan"]
word_2 = ["saya","suka","makan"]
def overlapping(a = [str], b=[str]):
    for i in a:
        for j in b:
            if (i == j):
                return True
    return False
print(overlapping(word_1,word_2))