
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


s = Stack()
s.push(1)
# s.push(2)
# s.push(3)
print(s)
print(s.pop())
print(s.pop())
print(s)
# print(s.peek())
# print(s)
# print(s.isEmpty())
