

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
# Stack is LIFO: Last in first out. For that append (add to end) each ele to a list and then
# access each ele using tail pointer.

def palindrome(link):
    l = link.size()
    stack = []
    current = link.getHead()
    count = -1
    mid = l//2

    while current != None:
        count = count + 1
        if count < mid:
            stack.append(current.getData())
        elif count == mid:
            if(l%2==0): # when len of linkedlist is even
                if(stack[-1] == current.getData()):
                    stack.pop()
                else:
                    return False
        else: # when count is greater than mid i.e 2nd half of list
            if(stack[-1] == current.getData()):
                stack.pop()
            else:
                return False

        current = current.getNext()

    return True




link = UnorderedList()
link.append(1)
link.append(2)
link.append(3)
link.append(2)
link.append(1)

print(link)
print(palindrome(link))
