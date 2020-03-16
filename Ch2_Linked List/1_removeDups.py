
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


# Solution 1: Uses temporary buffer
# def removeDups(link):
#     if link.isEmpty():
#         return False
#
#     num_set = [False]*100
#
#     current = link.getHead()
#
#     while current != None:
#         item = current.getData()
#
#         if(num_set[item]==True):
#             link.remove(item)
#         else:
#             num_set[item] = True
#
#         current = current.getNext()


# Does not use temporary buffer, instead uses 2 pointers: code runs in 0(1) space, but 0(N2) time.
def removeDups(link):
    if link.isEmpty():
        return False

    # pt1 at index 0
    pt1 = link.getHead()

    # pt2 at index 1
    # pt2 = link.getHead().getNext()

    while pt1.getNext() != None:
        pt2 = pt1.getNext()
        while pt2.getNext() != None:
            if(pt1.getData() == pt2.getNext().getData()):
                prev = pt2
                item = pt2.getNext()
                prev.setNext(item.getNext())
            pt2 = pt2.getNext()
        pt1 = pt1.getNext()


link = UnorderedList()

link.add(42)
link.add(13)
link.add(14)
link.add(13)

print(link)
removeDups(link)
print(link)
print("\n\n")
