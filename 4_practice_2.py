a = [2,3,4,5]
def is_member(x, a):
    for element in a:
        if element == x:
            return True
    return False
print(is_member(2,a))
