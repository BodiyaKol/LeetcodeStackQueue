class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.head = Node(x, self.head)
        self.size += 1
    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value
    def empty(self):
        return self.size == 0
    def peek(self):
        if self.empty():
            return None
        return self.head.data
class MyQueue(object):
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.push(x)
        return None
    def pop(self):
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()
    def empty(self):
        """
        :rtype: bool
        """
        return self.stack_in.empty() and self.stack_out.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
