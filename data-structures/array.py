class array:
    def __init__(self):
        self.__array = []
        self.__length = 0

    def push(self, item):
        self.__length += 1
        self.__array.append(item)
        return True

    def pop(self):
        if self.__length == 0:
            print("empty")
            return False
        self.__length -= 1
        return self.__array.pop()

    def insert(self, index, item):
        self.__array.insert(index, item)
        self.__length += 1
        return True

    def remove(self, index):
        if self.__length == 0:
            print("empty")
            return False
        self.__length -= 1
        return self.__array.pop(index)

    def print_array(self):
        print(self.__array)


if __name__ == "__main__":
    my_array = array()
    my_array.pop()
    my_array.remove(3)
    my_array.push(3)
    my_array.insert(0, 2)
    my_array.remove(0)
    my_array.pop()

    my_array.print_array()
