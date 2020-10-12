class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, data):
        self.__queue.insert(0, data)

    def dequeue(self):
        if len(self.__queue) > 0:
            return self.__queue.pop()
        return None

    def size(self):
        return len(self.__queue)


queue = Queue()
queue.enqueue('Mon')
queue.enqueue('Tue')
queue.enqueue('Wed')
print(queue.dequeue())
print(queue.dequeue())
print(queue.size())
queue.__queue = [1, 2, 3, 4, 5, 6, 7]
print(queue.dequeue())
