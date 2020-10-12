class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def pre_traversal(self, root):
        if root:
            print(root.data, sep=' ', end=' ')
            self.pre_traversal(root.left)
            self.pre_traversal(root.right)

    def middle_traversal(self, root):
        if root:
            self.middle_traversal(root.left)
            print(root.data, sep=' ', end=' ')
            self.middle_traversal(root.right)

    def post_traversal(self, root):
        if root:
            self.post_traversal(root.left)
            self.post_traversal(root.right)
            print(root.data, sep=' ', end=' ')


root = Tree(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root.middle_traversal(root)
print('')
root.pre_traversal(root)
print('')
root.post_traversal(root)
