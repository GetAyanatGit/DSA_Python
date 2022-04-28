'''
In this code we are going to understand how to append i.e
add an element at the end of a linked list
'''


#Basic Initializers

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, previous_node, new_data):
        if previous_node is None:
            print('No such previous node')
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
            
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


'''
Now, in order to append an element at the end of an existing linked list
we need to follow simply the following steps:

1. Make a new node with next as none/null
2. If the linked list is empty then make this new node as head
3. while the next is available continue
4. while the next is null assign the new node to it

Lets simply make a function --> append
'''

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

print('Linked list made with 3 elements 1,2,3')
llist.printlist()

'''

Appending an element to it

'''

llist.append(4)

print('After appending 4 at the end')
llist.printlist()








        

        
