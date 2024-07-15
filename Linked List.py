# CREATING NODES CLASS

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# CREATING LINKED LIST CLASS

class LinkedList:

    # INITILIZING LINKED LIST CLASS VARIABLES USING CONSTRUCTOR
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # PRINTING THE NODES OF LINKED LIST
    def print_list(self):
        temp = self.head
        if(temp == None):
            print('Linked List is empty to print')
        else:
            print('Element/s in the linked list is/are : ')
            while(temp != None):
                print(temp.value)
                temp = temp.next
            print('Linked List length is ', self.length)

    # ADDING A NEW NODE AT THE END OF THE LINKED LIST
    def append(self, value):
        new_node = Node(value)
        if(self.head != None):
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
    
    # REMOVING ALL NODES IN THE LINKED LIST
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    #  REMOVING THE LAST ELEMENT IN THE LIST
    def pop(self):
        prev = temp = self.head
        if(temp == None):
            print('Their are no elements to pop from the linked list')
        elif(self.length == 1):
            print('The poped element in the linked list is ', self.head.value)
            self.tail = self.head = None
            self.length = 0
        else:
            while(temp.next != None):
                prev = temp
                temp = temp.next
            self.tail = prev
            self.tail.next = None
            self.length -= 1
            print('The poped element in linked list is ', temp.value)
    
    # PREPENDING THE ELEMENT INTO THE LINKED LIST
    def prepend(self, value):
        new_node = Node(value)
        if(self.head == None):
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print('The prepended element is ', self.head.value)
        self.length += 1
    
    # POPING THE FIRST ELEMENT IN THE LINKED LIST
    def pop_first(self):
        if(self.head == None):
            print('Their are no elements in the linked list to pop')
        elif(self.length == 1):
            print('The first poped element in the linked list is ', self.head.value)
            self.tail = self.head = None
            self.length = 0
        else:
            print('The first poped element in the linked list is ', self.head.value)
            self.head = self.head.next
            self.length -= 1
    
    # GETTING THE INDEX VALUE FROM THE LINKED LIST
    def get(self, index):
        if(self.head == None):
            print('Their are no elements in the linked list to get')
        elif(index >= self.length or index < 0):
            print(f'Enter the index between 0 and {self.length} to get the values')
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            print('Element present in the given index is ', temp.value)
    
    # SETTING THE VALUE TO PARTICULAR INDEX (UPDATING THE VALUE)
    def set(self, index, value):
        if(self.head == None):
            print('Their are no elements in the linked list to set')
        elif(index >= self.length or index < 0):
            print(f'Enter the index between 0 and {self.length} to set the values')
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            temp.value = value
            print(f'Element i.e; {value} is setted at given index i.e; {index}')
    
    # INSERTING VALUE IN SPECIFIC POSITION IN LINKED LIST
    def insert(self, index, value):
        if(self.head == None):
            print('Their are no elements in the linked list to insert')
        elif(index >= self.length or index < 0):
            print(f'Enter the index between 0 and {self.length} to insert')
        else:
            new_node = Node(value)
            prev = temp = self.head
            if(index == 0):
                new_node.next = temp
                self.head = new_node
            else:
                for i in range(index):
                    temp = temp.next
                    if(i + 1 != index):
                        prev = temp
                new_node.next = prev.next
                prev.next = new_node
            self.length += 1
            print(f'The given element i.e; {value} is inserted at the given index i.e; {index}')

    # REMOVING THE SPECIFIC VALUE IN THE LINKED LIST
    def remove(self, index):
        if(self.head == None):
            print('Their are no elements in the linked list to remove')
        elif(index >= self.length or index < 0):
            print(f'Enter the index between 0 and {self.length} to remove')
        else:
            prev = temp = self.head
            if(index == 0):
                self.head = self.head.next
            else:
                for i in range(index):
                    temp = temp.next
                    if(i + 1 != index):
                        prev = temp
                prev.next = temp.next
            self.length -= 1
            print(f'The element i.e; {temp.value} is removed at the given index i.e; {index}')
    
    # REVERSING THE LINKED LIST
    def reverse_LL(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        print('After reversing the linked list ', end = '')



sll = LinkedList(10)
sll.append(20)
sll.print_list()
sll.make_empty()
sll.append(100)
sll.append(200)
sll.append(300)
sll.append(100)
sll.append(200)
sll.append(300)
sll.print_list()
sll.pop()
sll.print_list()
sll.prepend(0)
sll.print_list()
sll.pop_first()
sll.print_list()
sll.get(2)
sll.get(0)
sll.get(5)
sll.set(2, 57)
sll.set(1, 28)
sll.set(0, 50)
sll.print_list()
sll.insert(2, 10)
sll.print_list()
sll.remove(4)
sll.print_list()
sll.reverse_LL()
sll.print_list()