class queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)
        return True

    def dequeue(self):
        if len(self.__queue) == 0:
            print("empty queue")
            return False
        return self.__queue.pop(0)

    def isempty(self):
        return len(self.__queue) == 0

    def seek(self):
        if len(self.__queue) == 0:
            print("empty")
            return False
        return self.__queue[0]

    def print_queue(self):
        print(self.__queue)


if __name__ == "__main__":
    my_queue = queue()
    my_queue.dequeue()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    print(my_queue.seek())
    my_queue.dequeue()
    my_queue.print_queue()
