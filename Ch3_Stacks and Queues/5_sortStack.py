
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        if self.isEmpty():
            return('Stack is empty')
        st = ""
        for i in self.items:
            st = st + str(i) + ", "
        return "|"+ st[:-2] +"|"



def sortStack(inputStack):
    tempStack = Stack()

    while inputStack.isEmpty() != True:
        temp = inputStack.pop()
        while(tempStack.isEmpty()!=True and tempStack.peek() > temp):
            inputStack.push(tempStack.pop())
        tempStack.push(temp)

    return tempStack

s = Stack()
s.push(34)
s.push(3)
s.push(31)
s.push(98)
s.push(92)
s.push(23)
print(s)
print(sortStack(s))
