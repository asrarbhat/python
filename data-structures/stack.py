class stack:
    def __init__(self):
        self.__stack = []
        self.__length = 0

    def push(self, item):
        self.__length += 1
        self.__stack.append(item)
        return True

    def pop(self):
        if self.__length == 0:
            print("stack empty")
            return False
        self.__length -= 1
        return self.__stack.pop()

    def seek(self):
        if self.__length == 0:
            print("stack empty")
            return False
        return self.__stack[-1]

    def isempty(self):
        return self.__length == 0

    def print_stack(self):
        print(self.__stack)


if __name__ == "__main__":
    my_stack = stack()
    my_stack.pop()
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.pop()
    my_stack.pop()
    print(my_stack.isempty())
    my_stack.print_stack()
