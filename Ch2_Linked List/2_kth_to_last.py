# Linked List

class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def getData(self):
        # return int value
        return self.data

    def getNext(self):
        # returns object node
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
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


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


    def index(self, idx):
        current = self.head
        pos = -1
        while current != None:
            # index starts from 0
            pos = pos + 1
            if(pos == idx):
                return current.getData()

            current = current.getNext()


# Solution 1: When the LinkedList size is known, using index function
# def k_to_last(link, k):
#     l = link.size()
#     return link.index(l - k)


#Solution 2: When the LinkedList size is not know, using 2 pointers
def k_to_last(link, k):
    pt1 = pt2 = link.getHead()

    for i in range(k):
        if(pt2 == None):
            return False
        pt2 = pt2.getNext()

    while pt2 != None:
        pt1 = pt1.getNext()
        pt2 = pt2.getNext()

    return pt1.getData()


link = UnorderedList()
link.add(42)
link.add(13)
link.add(14)
link.add(15)
link.add(16)
link.add(17)

print(link)
print(k_to_last(link, 3))
