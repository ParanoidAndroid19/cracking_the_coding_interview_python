
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



# Solution 1: iterate through each list seperately, add each node data (digit) to a string
# reverse the string and convert it to int, then add the ints.
# Use for loop of range len(ints) and use add() to add them to resultant linkedlist

# When digits are stored in forward order:

# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295
# Output: 9 -> 1 -> 2, That is, 912.

# def sumList(link1, link2):
#     c1 = link1.getHead()
#     c2 = link2.getHead()
#     st1 = ""
#     st2 = ""
#
#     while c1 != None:
#         st1 = st1 + str(c1.getData())
#         c1 = c1.getNext()
#
#     while c2 != None:
#         st2 = st2 + str(c2.getData())
#         c2 = c2.getNext()
#
#     sum = int(st1) + int(st2)
#     char_sum = str(sum)
#     res = UnorderedList()
#
#     for i in range(len(char_sum)):
#         res.append(int(char_sum[i]))
#
#     return res
#
#
# link1 = UnorderedList()
# link1.append(6)
# link1.append(1)
# link1.append(7)
# print(link1)
#
# link2 = UnorderedList()
# link2.append(2)
# link2.append(9)
# link2.append(5)
# print(link2)
#
# print(sumList(link1, link2))


# When digits are stored in reverse order:

# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2) That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.

# def sumList(link1, link2):
#     c1 = link1.getHead()
#     c2 = link2.getHead()
#     st1 = ""
#     st2 = ""
#
#     while c1 != None:
#         st1 = st1 + str(c1.getData())
#         c1 = c1.getNext()
#
#     while c2 != None:
#         st2 = st2 + str(c2.getData())
#         c2 = c2.getNext()
#
#     sum = int(st1[::-1]) + int(st2[::-1])
#     char_sum = str(sum)
#     res = UnorderedList()
#
#     for i in range(len(char_sum)-1, -1, -1):
#         res.append(int(char_sum[i]))
#
#     return res


# Solution 2: In this, I do not convert the linked lists to integers, compute the sum,
# and then convert it back to a new linked list. I try to return the sum linkedlist without
# converting to an integer in process. To make LinkedLists have same lengths, I append zeros at the
# end of given list.

# When digits are stored in reverse order:

def sumList(link1, link2):
    c1 = link1.getHead()
    c2 = link2.getHead()
    res = UnorderedList()
    carry = 0
    sum = 0
    l1 = link1.size()
    l2 = link2.size()

    if l1 < l2:
        for i in range(l2 - l1):
            link1.append(0)
    else:
        for i in range(l1 - l2):
            link2.append(0)

    print(link1)
    print(link2)

    while c1 != None and c2 != None:
        sum = carry + c1.getData() + c2.getData()
        # selects the unit digit
        res.append(sum%10)
        # selects the one's digit
        carry = sum//10
        c1 = c1.getNext()
        c2 = c2.getNext()

    if carry > 0:
        res.append(carry)

    return res


link1 = UnorderedList()
link1.add(6)
link1.add(1)
link1.add(7)
print(link1)

link2 = UnorderedList()
link2.add(2)
link2.add(9)
link2.add(5)
print(link2)

print(sumList(link1, link2))
