
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

    def getHead(self):
        first = self.head
        return first

    def setHead(self, newHead):
        self.head = newHead

    def isEmpty(self):
        return self.head == None

    # item is added at the beginning of the list
    def add(self,item):
        # making item an instance/object of Node class
        temp = Node(item)
        # setting the previous head (1st ele) as next for newly added ele
        temp.setNext(self.head)
        # setting new ele as the head (1st ele of LL)
        self.head = temp
        return temp


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


    def remove(self,item):
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


    # adds ele at the end of the list
    def append(self, item):
        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        temp = Node(item)
        current.setNext(temp)
        temp.setNext(None)


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


# Solution 2: Apparantly I do not have access to even the head of LinkedList.
# Picture the list 1->5->9->12, Removing 9 would make it look like 1->5->12.
# You only have access to the 9 node. Can you make it iook like the correct answer?
def delNode(link, middle):
    middle.setData(middle.getNext().getData())
    middle.setNext(middle.getNext().getNext())


link = UnorderedList()
link.add(42)
link.add(14)
middle = link.add(15)
link.add(16)
link.add(17)
print(link)

# here middle is not an int, it is a node object, there can support getData and getNext methods.
link.delNode(middle)

# Solution 1: Simple, just use the remove function.
# In this I just use 2 pointers current and previous, and when current matches the item to be
# removed: previous.setNext(current.getNext()), this skips the current item and
# directly links the previous node's next to current node's next.

# link.remove(15)
# print(link)
