#13
verb = str(input("enter a word="))
def makeForms(verb):
    if verb[-1:] == "y":
        verb = verb[:-1] + "ies"
    elif verb[-1:] == ["o","s","x","z"] or verb[-2:] == ["ch","sh"]:
        verb = verb + "es"
    else:
        verb = verb + "s"
    print(verb)         
makeForms(verb)

verbs = [ "try","brush","run","fix"]
def makeFormwithS(verbs):
    new_verb = []
    for element in verbs:
        if element [-1:] == "y":
            new_verb.append(element[:-1] + "ies")
        elif element [-1:] in ["o","s","x","z"] or element[-2:] in ["ch","sh"]:
            new_verb.append(element + "es")
        else:
            new_verb.append(element + "s")
    print(new_verb)
makeFormwithS(verbs)
 
