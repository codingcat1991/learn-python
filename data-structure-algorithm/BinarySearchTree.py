class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()


# def insert_node(self, data):
#     node = Node(data)
#     if self.root is None:
#         self.root = node
#         return None
#     tag = ''
#     cur_node = self.root
#     while cur_node.left is not None:
#         if cur_node.data > data:
#             cur_node = cur_node.left
#         tag = 'left'
#     while cur_node.right is not None:
#         if cur_node.data < data:
#             cur_node = cur_node.right
#         tag = 'right'
#     if tag == 'left':
#         cur_node.left = node
#     else:
#         cur_node.right = node


top = BinarySearchTree(5)
top.insert(3)
top.insert(2)
top.insert(4)
top.insert(6)
top.insert(7)
top.insert(8)
top.print()
