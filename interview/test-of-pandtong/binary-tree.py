class BinaryTree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def preorder_recursion(self):
        if self.data:
            print(self.data, end=' ')
        if self.left:
            self.left.preorder_recursion()
        if self.right:
            self.right.preorder_recursion()

    def preorder_iteration(self):
        rst = []
        stack = [self]
        while stack:
            s = stack.pop()
            if s:
                rst.append(s.data)
                stack.append(s.right)
                stack.append(s.left)
        print(rst)

    def inorder_recursion(self):
        if self.left:
            self.left.preorder_recursion()
        if self.data:
            print(self.data)
        if self.right:
            self.right.preorder_recursion()

    def inorder_iteration(self):
        rst = []
        root = self
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            rst.append(root.data)
            root = root.right
        print(rst)

    def postorder_recursion(self):
        if self.left:
            self.left.preorder_recursion()
        if self.right:
            self.right.preorder_recursion()
        if self.data:
            print(self.data)

    def postorder_iteration(self):
        rst = []
        root = self
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                if root.left:
                    root = root.left
                else:
                    root = root.right
            s = stack.pop()
            rst.append(s.data)
            if stack and s == stack[-1].left:
                root = stack[-1].right
            else:
                root = None
        print(rst)

    def bfs(self):
        queue = [self]
        while queue:
            n = len(queue)
            for i in range(n):
                q = queue.pop(0)
                if q:
                    print(q.data, end=' ')
                    queue.append(q.left if q.left else None)
                    queue.append(q.right if q.right else None)

    def max_depth(self):
        if not self:
            return 0
        if not self.left and not self.right:
            return 1
        if not self.left:
            return 1 + self.right.max_depth()
        if not self.right:
            return self.left.max_depth()
        return 1 + max(self.left.max_depth(), self.right.max_depth())

    def min_depth(self):
        if not self:
            return 0
        if not self.left and not self.right:
            return 1
        if not self.left:
            return 1 + self.right.max_depth()
        if not self.right:
            return self.left.max_depth()
        return 1 + min(self.left.max_depth(), self.right.max_depth())

    def level_print(self):
        queue = [self]
        cnt = 0
        rst = []
        while queue:
            tmp = []
            n = len(queue)
            for i in range(n):
                q = queue.pop(0)
                if q:
                    if cnt % 2 == 0:
                        tmp = [q.data] + tmp
                    else:
                        tmp.append(q.data)
                    queue.append(q.left if q.left else None)
                    queue.append(q.right if q.right else None)
            rst.extend(tmp)
            cnt += 1
        return ''.join(rst)


#     A
#    / \
#   B   C
#  / \   \
# D   E   F

tree = BinaryTree(data='A')
tree.left = BinaryTree(data='B')
tree.right = BinaryTree(data='C')
tree.left.left = BinaryTree(data='D')
tree.left.right = BinaryTree(data='E')
tree.right.right = BinaryTree(data='F')
tree.level_print()

#              a          ---- level 0
#            /   \
#           b     c       ---- level 1
#          / \   / \
#         d   e f   g     ---- level 2
#        / \
#       h   i             ---- level 3


tree = BinaryTree(data='a')
tree.left = BinaryTree(data='b')
tree.right = BinaryTree(data='c')
tree.left.left = BinaryTree(data='d')
tree.left.right = BinaryTree(data='e')
tree.right.left = BinaryTree(data='f')
tree.right.right = BinaryTree(data='g')
tree.left.left.left = BinaryTree(data='h')
tree.left.left.right = BinaryTree(data='i')
tree.level_print()
