"""Author Heera Lal"""
class Node:
    """
    Create a class as node have having data and pointer
    """
    def __init__(self,data = None,next=None):
        self.data = data
        self.next = next
        
class Linked_List:
    def __init__(self):
        """Intialize a link list by creating head"""
        self.head = None
        
    def insert_at_begining(self,data):
        """Insert a value at the begining of the linked lust"""
        self.head = Node(data,self.head)
        
    def print(self):
        """ Print linked list for better understanding"""
        if self.head is None:
            print("List is empty")
        ll =""
        itr = self.head
        while itr:
            ll += str(itr.data) + "--->"
            itr = itr.next
        print(ll)
        
    def get_length(self):
        """Return current length of the linked list"""
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        #print("length of the linked list is =" , count)
        return count
        
    def insert_list(self,l):
        """Clear previous linked list and create a new one from a given python list"""
        self.head = None
        for i in l:
            self.insert_at_begining(i)
            
    def delete_at_begining(self):
        """ Delet staring element of linked list"""
        if self.head == None:
            return
        self.head = self.head.next
        
    def delet_at_end(self):
        """ Delet last element from linked list"""
        if self.get_length() ==0:
            print("list is empty")
            return
        if self.get_length() ==1:
            self.delete_at_begining()
            return
        count = 0
        itr = self.head
        while itr:
            if count == self.get_length()-2:
                itr.next = None
            count += 1
            itr = itr.next
        
    def delet_llist(self):
        """Delet entire linke list"""
        self.head = None
        
    def delet_at(self,ind):
        """Delet value from given index"""
        if ind<0 or ind>= self.get_length():
            print("Invalid index, please enter a valid index")
            return
        if ind == 0:
            self.delete_at_begining()
        count = 0
        itr = self.head
        while itr:
            if count == ind -1:
                itr.next = itr.next.next
                break
            count += 1  
            itr = itr.next
            
            
            
    def insert_at(self,ind,data):
        """insert value at given index"""
        if ind<0 or ind>= self.get_length():
            print("Invalid index, please enter a valid index")
            return
        if ind == 0:
            self.insert_at_begining()
        count = 0
        itr = self.head
        while itr:
            if count == ind -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            count += 1  
            itr = itr.next
            
    def delet_value(self,val):
        """Delet given value from linked list"""
        
        if self.head == None:
            return
        itr = self.head
        while itr.next:
            if itr.next.data == val:
                print(itr.next.data)
                itr.next = itr.next.next
                break
            itr = itr.next
        else:
            print("Value not fount in linked list")

        
            
    

if __name__ == "__main__":
    """ create a linked list and test functions or operations on it."""
    lls = Linked_List() 
    lls.insert_at_begining(6)
    lls.insert_at_begining(5)
    lls.insert_at_begining(2)
    lls.insert_at_begining(1)
    lls.print()
    print("="*100)
    lls.insert_list([9,8,7,4,5,6])
    lls.print()
    lls.get_length()
    lls.delete_at_begining()
    lls.print()
    lls.get_length()
    lls.delet_llist()
    lls.print()
    lls.get_length()
    print("="*100)
    lls.insert_list([9,8,6])
    lls.print()
    lls.get_length()
    lls.delet_at(3)
    lls.print()
    lls.get_length()
    lls.insert_at(2,11)
    lls.print()
    lls.get_length()
    lls.delet_at_end()
    print("="*100)
    lls.insert_list([9,5,7,4,8,6])
    lls.print()
    lls.delet_value(7)
    lls.print()
    print("="*100)
    lls.insert_list([9,5,7,4,8,6])
    lls.print()
    lls.delet_value(17)
    lls.print()
    
    
    
    
        
        

