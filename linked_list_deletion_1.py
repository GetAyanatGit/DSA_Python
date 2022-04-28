

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        print('__________________________________________________') 
        print('Printing the elements of the linked list')
        print('__________________________________________________') 
        while(temp):
            print(temp.data)
            temp = temp.next

    def del_node(self, key):
        ##1st store the head node
        temp = self.head
        ##Now the head node itself can hold the key to be deleted for
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        ## else search for the key to be deleted
        ## keep track of the previous and next nodes
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next

        ##finally if after searching till temp is none if key ot found
        if(temp is None):
            print('Element to be deleted not found')
            return

        prev.next = temp.next
        temp = None

llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.printlist()


# Pushing an element
llist.push(4)

llist.printlist()


'''
Iterative Method:
    
To delete a node from the linked list, we need to do the following steps. 
1) Find the previous node of the node to be deleted. 
2) Change the next of the previous node. 
3) Free memory for the node to be deleted.

'''

llist.del_node(4)

llist.printlist()








