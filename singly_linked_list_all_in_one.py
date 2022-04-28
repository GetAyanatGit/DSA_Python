'''
In this single piece of code we are going to make two classes two make linked lists. Linked Lists needs to objects to be
created, Data and Node. Data is inside the node and another variable points to the next node, thus making a chain of nodes.
Now once after making a linked list, we will be making a few methods in the linkedlist class to do some operations on the linked
list class we created.
'''


class Node:
    
    ## Making a node class, achain of node forms a nlinked list, so this is the elementary step since we will need object of this class
    ## to form a linked list
    ## Initializing a node object would keep two instance attributes for all instamces, a data & and 'next'
    ## which is a pointer to the next memory location
    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    ## This is the linked list class
    ## The first node is always the head node
    ## For the 1st time if a linked list is initialized and its having no elements
    ## i.e no nodes indeed, then the head node is going to be 'None'
    ## So, upon 1st initialization,in the constructor the head node is going to be null
    
    def __init__(self):
        self.head = None


    ## Since our linked list object is going to hold a number of nodes
    ## in a specified order, we will bring a custom print function to visualize them
    ## If there is an empty linked list, we already discussed, the head node is null
    ## So, if head of 'self' object is empty/none, that means the linked list is empty
    ## we will take an iterator object/declare it and string variable to store the elements in the list for output
    ## Now for the 1st time itr is self.head i.e the head node
    ## Then the 1st data is itr.data i.e the data of the head node
    ## Going forward, we will be picking the data of the next node of itr
    ## We will follow this till we get that the next node of present itr node is null
    ## When we will get the next node as null, that means we have reached the least node
    ## for other cases we will print ---> i.e mapping to
    ## but not for the last node
    ## once everything is done, result is the concatenated string 

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)


    ## We will now make a custom function to print the length of a linked list
    ## We already know that the next pointer of the last node is always null
    ## So we have to iterate uptill the last node and thus need to check whether the next node is null in every step
    ## and till it is not null we have to keep on adding the counter variable
    

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count


    ## We are going to make a function to insert an element at the front of the list
    ## As a parameter we will be passing the element to be inserted
    ## Now the algorithm to do the same is pretty easy, lets have a look at the following steps

    '''
    >> A new node object is instantiated with the new data
    >> The next of this new node is the head node, i.e the present 1st node
    >> Now this new node will be assigned hence considered as the head node or the 1st node
    '''
    

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    ## Note :: The time complexity of this function is O(1), since it only has statements to be executed, thus taking a constant time    


    ## Now we are going to make a function to insert an element at the end, i.e this element will be the last node's element now
    ## As a parameter we will be passing the data
    ## Now lets say if we only initialize a linked list but it is empty,so first we have to insert at least one node
    ## This node is the 1st node or the head node
    ## Initially its 'next' pointer is null
    ## So if the head none is null, i.e not yet any node is inserted
    ## the head node gets inserted
    ## Now while the 'next' node is not null i.e some pointer is available
    ## along the iteration through all the nodes' 'next' pointer
    ## keep moving, since the last node in the iterator will be the node with 'NULL' in next pointer
    ## Now its 'next' pointer would not be 'NULL' any more
    ## We will assign the new node to its 'next'

        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


    ## Note :: In python, better approach here is to use list where the complexity is O(1), but in linked list its O(n) for n elements.



    ## Now lets make a method that will accept a data and an index
    ## Will delink the nodes in that index and cross connect a new node
    ## at the specified index with your new data.Pretty interesting
    ## Lets have a look at the algorithm

    '''    
    >> An index in a linked list can never be negative, neither one can pass an index out of boundary
    >> So we are going to raise an exception an error if either of the two happens
    >> If one wants to insert data at begining insert_at_begining function needs to be called.
    >> If either of the above secanrios doesnt met then take a counter variable
    >> Since we have two delink the connection between the existing nodes, we have to stop, one node prior to node present at the the provided index
    >> At that point we have to stop create a new node object with the new data passed
    >> Attach the 'next' of our (index-1)th node to the new node
    >> The next of the new node will point to the indexth node.
    '''

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    ## Note :: Time complexity in this case for the worst case is going to be O(n) if the index is the last, best case 0(1) if first

            
    ## Now lets make a method that is going to remove the element at a sepcified index
    ## Again we have to keep the basic check of index boundaries
    ## If the index is 0, it means we are being told to remove the head node
    ## So now head node is next node i.e the next node is assigned to the head object
    ## If either of the above scenarios isn't met
    ## Keep checking with counter till the index - 1th element
    ## We always have to stop one node priot to the given index, remind, ***one step back in linked list***
    ## Stopping there the next of this node will now be pointing to the next of the indexth node, right? as the index node will be deleted        
            
            
            
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1


    ## Note ::  Deletion here is also claiming time complexity O(n) in the worst case and O(1) in the best cases in case of linked list       


    ## Now we are going to make another method which will make our task of making a linked list, easiest
    ## We are going to make a function i.e going to bind a linked list from a list passed as input parameter
    ## The approach is pretty simple
    ## data is iterated through the input list
    ## On every iteration, insert at end is called with the new data
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    ## Note :: Time Complexity of this approach is O(n) where n is the number of elements in the list.        


            


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
