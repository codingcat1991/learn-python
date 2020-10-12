class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        """入栈"""
        self.stack.append(data)

    def pop(self):
        """出栈"""
        if len(self.stack) <= 0:
            return None
        return self.stack.pop()

    def peek(self):
        """获取栈底元素"""
        return self.stack[0]


stack = Stack()
stack.push('Mon')
stack.push('Tue')
print(stack.peek())
stack.push('Wed')
stack.push('Thu')
print(stack.pop())
