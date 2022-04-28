
'''
This program explains the way to make a traversal through the linked list.
Here our approach is untill the next link is null, i.e the last element
of a linked list is reached our function printlist() within
the linked list class will print all the elements.
'''

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init_(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.printlist()

