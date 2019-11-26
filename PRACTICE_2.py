
#1
def List(list):
    New_list = []
    for element in list:
        element = str(element)
        New_list.append(element)
    print(New_list)
    print(tuple(New_list))

List ([2,3,4,5])

#2
def translate(text):
    vowels = ["a","i","u","e","o"," "]
    letters = ""
    for letter in text:
        if letter in vowels:
            letters = letters + letter
        else:
            letters = letters + letter + "o" + letter
    print(letters)

translate("This is fun")

#3


#4
val = [2,"mama","saya",3,4,5]
def is_member(val):
    x = 4
    for element in val:
        if element == x:
            return True
    return False
print(is_member(val))


#6
def histogram(lst):
    for i in lst:
        print("*" * i)
histogram([4,5,7])

#7

word_list = ["maap","sorry","saya","mantap"]
print(word_list)
length_of_word = []
for word in word_list:
    length_of_word.append(len(word))
print(length_of_word)

#8
lword =  ["mantap","lol"]
def find_longest_word(lword):
    longest_length = 0
    for elements in lword:
        if len(elements) > longest_length:
            longest_length = len(elements)
    return longest_length


print(find_longest_word(lword))



        




        





