# compare two strings to see if they have overlapping letters

def twoStrings(s1, s2):
    # 1. convert strings into sets (ex: {'s','t','r','i','n','g'})
    s1 = set(s1)
    s2 = set(s2)
    # 2. set.intersection(set2) will return elements that occur in both sets
    result = s1.intersection(s2)
    if result:
        return "YES"
    return "NO"