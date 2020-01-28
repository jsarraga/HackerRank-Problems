# add the numbers to the set incrementally and check if the complement was already present in the set.

def pairs(k, arr):
    numbers = set()
    count = 0
    for n in arr:
        # checking if complements are in the set. If n + k is in the set, there is a pair == count +=1
        if n + k in numbers:
            count += 1
        # checking if complements are in the set. If n - k is in the set, there is a pair == count +=1
        if n - k in numbers:
            count += 1
        numbers.add(n)
    return count


k = 2
arr = [1, 5, 3, 4, 2]

print(pairs(k,arr))