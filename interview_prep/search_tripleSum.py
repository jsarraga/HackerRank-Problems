

# p <= q and q =< r


def triplets(a, b, c):
    # set only takes in UNIQUE numbers aka removes duplicates
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    
    result = 0

    for i in range(len(b)):
        a_counter = 0
        c_counter = 0


        for j in a:
            if j <= b[i]:
                a_counter +=1
        for k in c:
            if k <= b[i]:
                c_counter += 1
        
        result += a_counter * c_counter
    
    return result


a = [1, 4, 5]
b = [2, 3, 3]
c = [1, 2, 3]

print(triplets(a,b,c))