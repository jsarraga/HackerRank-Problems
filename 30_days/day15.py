# Day 15: Linked Lists
#  create insert funciton of the class


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        newNode = Node(data)  # create a new node instance passing data through
        if head is None:    # check to see if we are starting a new list
            return newNode  # if head is none, return newNode as head
        current = head  # set a reference to our current node starting at the head
        while current.next:   # check if there is a next node
            current = current.next  # jump to next node by setting reference to next node
        current.next = newNode  # we reach end of list when current node has no next node. exit while. set current node next reference to new node to insert at the end of the list
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  