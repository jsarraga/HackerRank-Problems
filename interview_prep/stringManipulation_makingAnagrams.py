from collections import Counter

def makeAnagram(a, b):
    c1 = Counter(a) # makes a dictionary of the characters and frequencies as keys
    c2 = Counter(b)
    return sum(((c1-c2)+(c2-c1)).values()) # takes the difference from each dict and combines values into one dict