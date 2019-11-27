english_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"] 
def check_sentence(text):
    text = text.casefold()
    text = text.lower()
    for letter in text:
        if letter in english_letter:
            english_letter.remove(letter)
    if len(english_letter) == 0:
        print("pangram")
    else:
        print("not pangram")

print(check_sentence(" The quick brown fox jumps over the lazy dog"))