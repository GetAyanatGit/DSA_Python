

class Node:
    
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        str_list = ''
        itr = self.head
        while itr:
            if itr.next:
                str_list = str_list + str(itr.data) + '  <----->  '
            else:
                str_list = str_list + str(itr.data)
            itr = itr.next
        print(str_list)

    def insert_at_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        
        
        while(itr.next):
            itr = itr.next

        new_node = Node(data)
        itr.next = new_node
        new_node.prev = itr


    def make_dll_from_list(self,elements):
        for element in elements:
            self.insert_at_end(element)

    def getLength(self):
        counter= 0
        if self.head is None:
            return counter
        itr = self.head
        while(itr.next):
            itr = itr.next
            counter += 1

        return counter+1   

    def insertAt(self, index, element):
        if index<0 or index>self.getLength():
            raise Exception("Index Out of Boundary Error")
            return

        if index == 0:
            self.insert_at_front(element)
            return

        counter = 0
        itr = self.head
        while(itr.next):
            if index == counter:
                new_node = Node(element)
                new_node.prev = itr
                new_node.next = itr.next
                itr.next = new_node
                break
            counter += 1

            

     def removeAt(self,index,element):
         if index<0 or index>self.getLength():
            raise Exception("Index Out of Boundary Error")
            return

         if index == 0:
             self.head = self.head.next
             return
            
         counter = 0
         itr = self.head
         while(itr.next):
             if index - 1 == counter:
                 itr.next = itr.next.next
                 break
             itr = itr.next
             count += 1
            
            


##dll = DoubleLinkedList()
##dll.head = Node(1)
##second = Node(2)
##third = Node(3)
##
##dll.head.next = second
##second.next = third
##
##third.prev = second
##second.prev = dll.head
##
##dll.print()
##
##dll.insert_at_front(5)
##
##dll.print()
##
##
##dll.insert_at_end(6)

            
dll = DoubleLinkedList()
dll.make_dll_from_list([1,2,3,4,5,6,7,8,9])
dll.print()

print(dll.getLength())

dll.insertAt(2,10)
dll.print()




