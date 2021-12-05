from typing import TypeVar
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node
        

# Defines the singly linked list
class LinkedList:
    def __init__(self):
      self.head = None #keep the head private.Not accessible outside class
      self.len = 0
      self.tail = None
      self.max = None

    
    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1) It is constant because it doesn't depend on how big the data input is
    # Space Complexity: O(1) Constant doesn't depend on size of input
    def get_first(self):
        if self.head == None:
            return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: 4 operations 4 * big O(1) 
    # Space Complexity: It always creates one node so O(1); if you have n elements then it would be O(n). 
    def add_first(self, value):
        # next_node = self.head
        self.head = Node(value, next_node = self.head) #creating 0(1)
        self.len += 1
        #result = isinstance(self.head, int )
        #if result:
        if type(value) is int:
            self.update_max(value) # 0
        

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n) because it searches everything in list.  If it was a phone book it would jump to where letter starts then it would be O log(n) because it would cut in half. Another example of 0 log(n)would be binary search tree where it cuts in half
    # Space Complexity: O(1) because zero is a constant 
    def search(self, value):
        node = self.head
        while node != None:
            if node.value != value:
                node = node.next
            else:
                return True
        return False
        
        

    # method that returns the length of the singly linked list
    # Time Complexity: Everytime I call this function how much more time does it take given how big input is. O(1) in this case because it is going directly to length
    # Space Complexity: every time i call this function how much more memory is computer going to use? In this case it doesn't use more memory so O(1)
    def length(self):
        if self.head == None:
            return 0
        return self.len

            
    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n) because it is looping through linked list and the linked list size can change.
    # Space Complexity: I am not allocating memory I use a constant variable for counter so it is 0(1). An example is counting a number of cars in a lot. I need to find car total.  Even though I am counting all the cars I just store total count.    Very rare to have time complexity be  less than space complexity.  Usually if you do something with memory you are also doing it with time.   
    def get_at_index(self, index):
        node = self.head
        counter = 0
        if self.len < index:
            return None
        while node != None:
            
            if counter == index:
                return node.value
            node = node.next
            counter +=1 
        return None

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(1) because I am going straight to the index
    # Space Complexity: O(1) Constant doesn't depend on size of input
    def get_last(self):
        print(self.len)
        return self.get_at_index(self.len-1)
        
       
    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(1) because you are adding 1 node 
    # Space Complexity: O(1) because you are updating the max variable
    def add_last(self, value):
        
        if self.len == 0:
            self.tail = Node(value, next_node = None)
            self.head = self.tail
            self.update_max(value)

        else:
            self.tail.next = Node(value, next_node = None)
            self.tail = self.tail.next
            self.update_max(value)
        
        self.len += 1 
        

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        return self.max

    def update_max(self,value):
        if self.max == None: 
            self.max = value 
     
        if value >= self.max:
            self.max = value

        

    # method to delete the first node found with specified value
    # Time Complexity: O(n) because you are looping through all the values until you get the right one.  
    # Space Complexity: O(1) because it is updating the variables
    def delete(self, value):
        node = self.head
        prev_node = None
        while node != None:
            if node.value != value:
                prev_node = node
                node = node.next
            else:
                if prev_node == None:
                    self.head = node.next
                    self.len -= 1
                else:
                    prev_node.next = node.next
                    self.len -= 1 
                break
               
        

    # method to print all the values in the linked list
    # Time Complexity: 0(n) it is looping through each value 
    # Space Complexity: 0(n) it is creating an array of all the nodes
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n) it is looping through all of the nodes
    # Space Complexity: 0(1) because it just using the same variables and only updating the values
    def reverse(self):
        prev = None
        current = self.head
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: 
    # Space Complexity: 

    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
