# Day 14: Scope

"""
For unorganized arrays, complexity will always be O(n2) because we'll have to compare each element to each other
if we were to go through every element.

To make it linear, we know that we'll only really need the difference between the highest and lowest elements for 
the max difference.
"""

class Difference:
    def __init__(self, a):
        self.__elements = a

        #Write code here
        self.maximumDifference = 0

    def computeDifference(self):
        min_element = 101 #Constraints given by the problem 
        max_element = 0  
        for element in self.__elements:
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element
        
        self.maximumDifference = max_element - min_element
   
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)