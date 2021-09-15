class Graph:
    def __init__(self):
        self.__graph = {}

    def graph(self):
        return self.__graph

    def add_node(self, node):
        if not isinstance(node, (str,)):
            print("node name must be a string")
            return False
        elif node in self.__graph.keys():
            print("node already exists")
            return False
        self.__graph[node] = []
        return True

    def add_edges(self, node, to):
        node_added = self.add_node(node)
        if not node_added:
            return False
        if not isinstance(to, (list, tuple, set))
