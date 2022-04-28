
'''
In this code we are going to understand how to insert an element
at a given position in between two nodes in a linked list. i.e basically
after a given node
'''

## Basic Initializers

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def add_from_front(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, previous_node, new_data_for_new_node):
        if previous_node is None:
            print('There is no previous such node')
            return
        
        new_node = Node(new_data_for_new_node)
        new_node.next = previous_node.next
        previous_node.next = new_node


    
'''
Now, lets consider a linked list : 1,2,3
Lets consider a new element 5 to be inserted between Node 2 and 3
The required steps should be :

1. We need to check whether any previous node is available
2. If available then we need to 1st make a new node
3. Assign the next of previous node to the next of this new node
    e.g the next node of 2 was 3, but now the next ode of 5 will be 3
4. Assign this new node as the next node of previous node
    e.g the next node of 2 will now be 5

So to implement all these we will make a function inside the linkedlist
class <<insert_after>>
'''

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

print('Before Insertion after node 2')
llist.printlist()

print('After insertion after node 2')
llist.insert_after(second,5)
llist.printlist()














