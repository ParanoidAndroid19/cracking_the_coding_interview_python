

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

    def getTail(self):
        last = self.tail
        return last

    def setTail(self, newTail):
        self.tail = newTail

    def isEmpty(self):
        return self.head == None


    # item is added at the beginning of the list
    def add(self,item):
        temp = Node(item)
        if self.head == None:
            self.tail = self.head = temp
        else:
            temp.setNext(self.head)
            self.head = temp


    # adds ele at the end of the list
    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.tail = self.head = temp
        else:
            self.tail.setNext(temp)
            self.tail = temp
        return self.tail


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


def intersect(link1, link2):
    c1 = link1.getHead()
    c2 = link2.getHead()

    t1 = link1.getTail()
    t2 = link2.getTail()

    intersect = False

    if t1 == t2:
        intersect = True
    else:
        return False


    while c1 != None:
        c2 = link2.getHead()
        while c2 != None:
            # print(c1.getData())
            # print(c2.getData())
            # print("\n")
            if c1 == c2:
                return c1.getData()
            c2 = c2.getNext()
        c1 = c1.getNext()

    return False


same = Node(7)
last = Node(2)
same.setNext(last) # the tail

link1 = UnorderedList()
link1.append(3)
link1.append(1)
link1.append(5)
# link1.append(9).setNext(same)
# link1.setTail(same.getNext())



link2 = UnorderedList()
link2.append(4)
# link2.append(6).setNext(same)
# link2.setTail(same.getNext())

print(link1)
print(link2)
print(intersect(link1, link2))
