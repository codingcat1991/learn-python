# 1.	Code exercise – Print binary tree
#
# implement level print function, which print binary tree level by level
# and print even level from right to left while odd level from left to right
#
# example:
# supposed there is a binary tree like below
#               a          ---- level 0
#             /   \
#            b     c       ---- level 1
#           / \   / \
#          d   e f   g     ---- level 2
#         / \
#        h   i             ---- level 3
#
# output should be this: abcgfedh
#
# TreeNode class is the binary tree node
class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def level_print(tree_root):
    queue = [tree_root]
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


if __name__ == "__main__":
    tree = TreeNode(data='a')
    tree.left = TreeNode(data='b')
    tree.right = TreeNode(data='c')
    tree.left.left = TreeNode(data='d')
    tree.left.right = TreeNode(data='e')
    tree.right.left = TreeNode(data='f')
    tree.right.right = TreeNode(data='g')
    tree.left.left.left = TreeNode(data='h')
    tree.left.left.right = TreeNode(data='i')
    print(level_print(tree))
