
# Linked List
class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:

    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        # head points to the first ele of the list
        self.head = None
        self.tail = None

    def getHead(self):
        first = self.head
        return first

    def setHead(self, newHead):
        self.head = newHead

    def isEmpty(self):
        return self.head == None


    # item is added at the beginning of the list
    def add(self,item):
        # # making item an instance/object of Node class
        # temp = Node(item)
        # # setting the previous head (1st ele) as next for newly added ele
        # temp.setNext(self.head)
        # # setting new ele as the head (1st ele of LL)
        # self.head = temp
        # return temp
        temp = Node(item)
        if self.head == None:
            self.tail = self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp
        return temp


    # adds ele at the end of the list
    def append(self, item):
        # current = self.head
        #
        # while current.getNext() != None:
        #     current = current.getNext()
        #
        # temp = Node(item)
        # current.setNext(temp)
        # temp.setNext(None)
        if self.head == None:
            self.tail = self.head = Node(item)
        else:
            self.tail.setNext(Node(item))
            self.tail = self.tail.getNext()


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count


    def __str__(self):
        current = self.head
        st = ""
        while current != None:
            st = st + str(current.getData())+"-->"
            current = current.getNext()
        return st+"||"


    def search(self, item):
        current = self.head

        while current != None:
            if(item == current.getData()):
                return "Found"
            current = current.getNext()
        return "Not Found"


    def remove(self, item):
        current = self.head
        previous = None
        found = False

        # loop will go on till found = False
        while found == False and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found == True:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            print("Element not found")


    # removes and returns the last item
    def pop(self):
        current = self.head
        previous = None

        while current.getNext() != None:
            previous = current
            current = current.getNext()

        previous.setNext(None)
        return current.getData()


    # to return element at a particular index
    def index(self, idx):
        current = self.head
        pos = -1
        while current != None:
            # index starts from 0
            pos = pos + 1
            if(pos == idx):
                return current.getData()

            current = current.getNext()


# Solution 1:
# In this I will make x/partition one node and start from it. I will iterate through the given linkedlist and
# if the node is less than x then make x as next of the node,
# if node is greater then or equal to x then make the node next of x.
# Finally, remove x (since you added it) using the next.next method.
def partition(link, x):
    new = UnorderedList()
    current = link.getHead()

    while current != None:
        data = current.getData()
        if(data < x):
            # adding at the beginning of the list
            new.add(data)
        else: # data is equal to or grater than x
            # adding at the end of the list
            new.append(data)
        current = current.getNext()

    return new



link = UnorderedList()
link.add(3)
link.add(5)
link.add(8)
link.add(10)
link.add(2)

print(link)

print(partition(link, 5))


# EXAMPLES:
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
# [partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# Input : 1->4->3->2->5->2->3,
#         x = 3
# Output: 1->2->2->3->3->4->5

# Input : 1->4->2->10
#         x = 3
# Output: 1->2->4->10

# Input : 10->4->20->10->3
#         x = 3
# Output: 3->10->4->20->10
