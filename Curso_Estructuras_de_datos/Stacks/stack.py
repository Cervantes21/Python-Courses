from nodos import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        
        else:
            self.top = node

        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next

            else:
                self.top = None

            return data
        
        else:
            return 'The stack is empty'

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return 'The Stack is empty'

    def clear(self):
        while self.top:
            self.pop()

