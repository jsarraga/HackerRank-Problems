"""
Day 8: Dictionaries and Maps

Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Sample Input

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry


Sample Output

sam=99912222
Not found
harry=12299933
"""


n = int(input())

for i in range(n):
    data = str(input()).split(" ")

    name = data[0]
    phone = data[1]

    phonebook[name] = phone

for j in range(n):
    name = str(input())

    if name in phonebook:
        phone = phonebook[name]
        print(name + "=" + phone)
    else:
        print("Not found")