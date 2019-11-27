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