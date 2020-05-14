class Stack:
    def __init__(self):
        self.items = []
        self.mStack = []
        # self.poppedList = {}

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.minStack_push(item)

    def minStack_push(self, item):
        if(self.mStack == []):
            self.mStack.append(item)
        else:
            if self.mStack[-1] > item:
                self.mStack.append(item)

    def minStack_pop(self, item):
        # that is top of stack, the min
        if item == self.mStack[-1]:
            self.mStack.pop()

    def min(self):
        return self.mStack[-1]

    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        popped = self.items.pop()
        self.minStack_pop(popped)
        return popped


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


s = Stack()
s.push(7)
s.push(8)
s.push(2)
s.push(5)
print(s)
print(s.pop())
print(s.pop())
print(s)
print("Min: " + str(s.min()))
