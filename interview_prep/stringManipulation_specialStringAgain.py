def substrCount(n, s):
    count = 0
    for i in range(n-1):
        count += 1
        if s[i+2] == 0 or s[i+1] == 0:
            count += 1
        elif s[i] == s[i+2]:
            count += 1
        elif s[i] == s[i+1] and s[i] == s[i+2]:
            count += 1
    return count 

n = 7
s= "abcbaba"
print(substrCount(n,s))