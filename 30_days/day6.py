"""

Let's Review 

Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed 
characters as  space-separated strings on a single line (see the Sample below for more detail).

sample input:
2
Hacker
Rank

sample output
Hce akr
Rn ak
"""


n = int(input())

for i in range(0,n):
    string = input()

    for j in range(len(string)):
        if j % 2 == 0:
            print(string[j], end ='')

    print(" ", end ='')

    for j in range(len(string)):
        if j % 2 != 0:
            print(string[j], end ='')
    
    print(" ")
