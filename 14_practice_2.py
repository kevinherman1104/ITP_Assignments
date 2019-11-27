#14
verb = ["go","lie","see","move"," hug"]
def makeForming(verb):
    verb_ing = []
    for element in verb:
        if element[-1:] == "e" and element not in ["be","see","flee","knee"] and element[-2:] != "ie":
            verb_ing.append(element[:-1] + "ing")
        elif element [-2:] == "ie":
            verb_ing.append(element[:-2] + "ying")
        elif element [-1:] not in ["a","i","u","e","o"]:
            verb_ing.append(element + element[-1] + "ing")
        else:
            verb_ing.append(element + "ing")        
    print(verb_ing)         
makeForming(verb)

 