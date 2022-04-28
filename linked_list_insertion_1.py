
'''
A node can be added in three ways 

1) At the front of the linked list 
2) After a given node. 
3) At the end of the linked list.

'''

#Making necessary classes for linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def new_node_from_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
            

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

print('--------------------------------------------------------')
print('Creating Linked List with 1,2 and 3 and then printing it')
llist.printlist()
print('--------------------------------------------------------')




#1) Adding element at the front of the linked list

'''
If 4 is added to 1-->2-->3 at the front
then new linked list would look like
4 --> 1 --> 2--> 3
Which means 4 should be the head node now
The next of this Node"4" should point to Node"1"
So, we will implement the following with the below  steps

1. Create a new Node with New data "4"
2. Assign current head node (Node_1) as its next node
3. Assign it as the current head node

For the same we have made a function inside LinkedList Class itself
<<new_node_from_front function>>

'''

llist.new_node_from_front(4)
print('--------------------------------------------------------')
print('Inserting 4 from front and then printing it')
llist.printlist()
print('--------------------------------------------------------')


'''
We call this above operation as push and the time complexity
of this mechanism is O(1) as it does a constant amount of work.
'''










