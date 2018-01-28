#!/opt/bin/python

def isUnique(word):
    counter = []
    
    for c in list(word):
        if c not in counter:
            counter.append(c)
        else:
            return False

    return True

print(isUnique("hey"))
print(isUnique("bobo"))
