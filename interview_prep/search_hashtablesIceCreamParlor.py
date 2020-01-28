#  DID NOT PASS TEST CASES IN HACKERRANK


# For each value, check if the compliment is in the keys of the map. 
# If it is then you've found your pair, duplicate or not. 
# If it isn't then add the cost of the flavour to the map. 
# O(n) and you don't need any special consideration for the case when the answer is two ice creams with the same cost.

def whatFlavors(cost, money):
    map = {}
    # for pos, cost in enumerate(cost):
    #     if cost in map:
    #         return (map[cost], pos + 1)
    #     else:
    #         map[money - cost] = pos + 1

    # OR
    
    for pos, cost in enumerate(cost):
        compliment = money - cost
        if compliment in map:
            return (map[compliment], pos + 1)   #map[compliment] is index of cost of flavor complimentary to current cost | pos+1 is index of current cost 
        else:
            map[cost] = pos + 1 # adding index of current cost to map
        



money = 4
n = 5
cost = [1, 4, 5, 3, 2]        

print(whatFlavors(cost, money))
