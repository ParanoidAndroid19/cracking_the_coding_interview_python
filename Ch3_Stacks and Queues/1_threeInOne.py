
# Here we are assuming the stacks sizes are predifined and they cannot exceed that size

class MultiStack:

    def __init__(self, capacity):
        self.numStacks = 3  #number of stacks in array
        self.array = [0] * (capacity * self.numStacks)  #thus the len of array is 2 * 3 = 6
        self.sizes = [0] * self.numStacks  # to record the no. of filled indices in each stack
        self.capacity = capacity  #The capacity of each stack i.e 2

    # stackNum is the number tag of stacks, like 1st stack, 2nd stack, etc
    def push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception("Stack is full")
        self.sizes[stackNum] += 1  # stack size is increased since 1 ele is pushed
        self.array[self.topIndex(stackNum)] = item

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is empty')
        popped = self.array[self.topIndex(stackNum)]
        self.array[self.topIndex(stackNum)] = 0
        self.sizes[stackNum] -= 1
        return popped

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is empty')
        return self.array[self.topIndex(stackNum)]

    def topIndex(self, stackNum):
        offset = stackNum * self.capacity  #for 0th stack: 0 * 2
        return offset + self.sizes[stackNum] - 1  # 0 + 0 - 1

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.capacity

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    def __str__(self):
        st = ""
        for i in range(len(self.array)):
            st = st + str(self.array[i]) + ', '
        return '|' + st[:-2] + '|'



new = MultiStack(2)
new.push(3, 1)
new.push(2, 1)
print(new)
print(new.isEmpty(0))
print(new.pop(1))
print(new)
print(new.peek(0))
