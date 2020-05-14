
class SetOfStacks:
    def __init__(self, capacity):
        self.items = []  # the current stack
        self.stackSet = []  # will store the filled stacks, ones the items stack is full append it here and then items = []
        self.capacity = capacity


    def isEmpty(self):
        return self.items == []


    # if the whole set of stacks is empty
    def allEmpty(self):
        # stackSet = [] or stackSet = [[]]
        if(len(self.stackSet)==0 or len(self.stackSet[0])==0):
            return True
        else:
            return False


    # has the current stack reached its capacity?
    def isFull(self):
        return len(self.items) == self.capacity

    def push(self, item):
        # if the stack previous to the current stack (items) is empty then remove it since the new elements would now be pushed to current stack
        if len(self.stackSet) != 0:
            if len(self.stackSet[-1]) == 0:
                self.stackSet.remove(self.stackSet[-1])

        if self.isFull():
            self.stackSet.append(self.items)
            self.items = []
            self.items.append(item)
        else:
            self.items.append(item)


    def pop(self):
        # if the current stack is empty (items)
        if self.isEmpty():
            # if all stacks are empty
            if self.allEmpty():
                return("Stack is empty")
            else:
                # the top most (last) non-empty stack
                return self.stackSet[-1].pop()

        return self.items.pop()


    def popAt(self, index):
        if self.allEmpty():
            return("Stack is empty")

        if len(self.stackSet[index])==1:
            popped = self.stackSet[index].pop()
            self.stackSet.remove(self.stackSet[index])
            return popped

        return self.stackSet[index].pop()



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



s = SetOfStacks(2)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# s.push(11)
# s.push(12)
# s.push(13)

print(s.popAt(0))
print(s.popAt(0))
s.push(11)
s.push(12)
