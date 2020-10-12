class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """在链表最后添加节点"""
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        node.prev = cur_node
        cur_node.next = node

    def add_first(self, data):
        """在链表头添加节点"""
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        self.head, node = node, self.head
        self.head.next = node
        node.prev = self.head

    def insert(self, node, data):
        if node is None:
            return
        if node.next is None:
            self.append(data)
        new_node = Node(data)
        next_node = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = next_node
        next_node.prev = new_node

    def print(self):
        cur_node = self.head
        print('None<-', end='')
        while cur_node:
            print(cur_node.data, end='')
            if cur_node.next is not None:
                print('<=>', end='')
            cur_node = cur_node.next
        print('->None')


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append('Mon')
doubly_linked_list.append('Tue')
doubly_linked_list.append('Wed')
doubly_linked_list.print()
doubly_linked_list.add_first('Sat')
doubly_linked_list.print()
doubly_linked_list.insert()
