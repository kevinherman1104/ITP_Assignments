string = "i have a dog"
string = string.casefold()

def char_freq(string):
    freq = {}
    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] =1
    print(freq)
char_freq(string)