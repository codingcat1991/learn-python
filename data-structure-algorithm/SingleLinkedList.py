class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        """遍历链表"""
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end='->')
            cur_node = cur_node.next
        print('None')

    def insert_first(self, data):
        """在链表的开始插入"""
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        """在链表末尾插入"""
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def add(self, node, data):
        """在指定节点后添加新节点"""
        if node is None:
            print('The mentioned node is absent')
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def delete(self, data):
        """删除指定节点，第一个节点没有前驱节点，需单独处理"""
        cur_node = self.head
        if cur_node is not None:
            if cur_node.data == data:
                self.head = cur_node.next
                cur_node = None
                return
        # 找到指定数据所在节点的前驱节点
        while cur_node:
            if cur_node.next.data == data:
                break
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next


linked_list = SingleLinkedList()
linked_list.head = Node('Mon')
node2 = Node('Tue')
node3 = Node('Wed')
linked_list.head.next = node2
node2.next = node3
linked_list.print()
linked_list.insert_first('Thu')
linked_list.print()
linked_list.append('Sat')
linked_list.print()
linked_list.add(node2, 'Sun')
linked_list.print()
linked_list.delete('Thu')
linked_list.print()
