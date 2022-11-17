class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}
        for start, end in self.edges:
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append(end)
            else:
                self.graph_dictionary[start] = [end]

    def __str__(self):
        return str(self.graph_dictionary)

    def add_vertex(self, vertex):
        if vertex not in self.graph_dictionary:
            self.graph_dictionary[vertex] = []

    def delete_vertex(self, vertex):
        if vertex in self.graph_dictionary:
            del self.graph_dictionary[vertex]

    def add_edges(self, vertex, edge):
        if vertex not in self.graph_dictionary:
            self.add_vertex(vertex)

        self.graph_dictionary[vertex].append(edge)

    def deleting_edge(self, vertex, edge):
        if vertex in self.graph_dictionary:
            my_list = list(self.graph_dictionary[vertex])
            deleting_index = my_list.index(edge)
            del self.graph_dictionary[vertex][deleting_index]
            # del self.graph_dictionary[edge][vertex]

    def get_all_neighbours(self, vertex):
        return self.graph_dictionary.get(vertex, "No assigned vertex")


    def dfs(self, vertex):
        path = []

        stack_val = [vertex]

        while len(stack_val) != 0:

            element = stack_val.pop()

            if element not in path:
                path.append(element)
            if element not in self.graph_dictionary:
                # leaf node
                continue

            for neighbor_node in self.graph_dictionary[element]:
                stack_val.append(neighbor_node)
        return path[:-1]
        #return DfsIterator(self, vertex)


    def bfs(self, vertex):
        path = []
        visited = [vertex]

        while len(visited) != 0:  
            element = visited.pop()
        

            if element not in path:
                path.append(element)
            if element not in self.graph_dictionary:
                
                continue

            for neighbour in self.graph_dictionary[element]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    path.append(neighbour)
            path = path[:-1]
        return (path)

        # return BfsIterator(self, vertex)


# class DfsIterator:
#     def __init__(self, graph, vertex):
#         self.graph = graph
#         self.vertex = vertex
#         self.path = []
#         self.stack_val = [vertex]
#
#         while len(self.stack_val) != 0:
#
#             element = self.stack_val.pop()
#
#             if element not in self.path:
#                 self.path.append(s)
#             if element not in graph.get_all_neighbours(self.vertex):
#
#                 continue
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             return self.path
#         except IndexError:
#             raise StopIteration
#
# class BfsIterator:
#
#     def __init__(self, graph, vertex):
#         self.graph = graph
#         self.path = []
#         self.visited = [vertex]
#
#         while len(self.visited) != 0:
#             element = self.visited.pop()
#             if element not in self.path:
#                 self.path.append(element)
#             if element not in self.graph:
#                 continue
#
#             for neighbour in graph.get_all_neighbours(self.vertex):
#                 if neighbour not in self.visited:
#                     self.visited.append(neighbour)
#                     self.path.append(neighbour)
#             self.path = self.path[:-1]
#
#     def __next__(self):
#         try:
#             return self.path
#         except IndexError:
#             raise StopIteration
#
#     def __iter__(self):
#         return self

if __name__ == '__main__':

    connections = [
        ("Krakow", "Warszawa"),
        ("Warszawa", "Kraków"),
        ("Warszawa", "Gdansk"),
        ("Krakow", "Gdansk"),
        ("Krakow", "Wieden")
    ]

    graph = Graph(connections)
    print(graph)

    graph.add_vertex("Poznań")
    print(graph)

    graph.delete_vertex("Poznań")
    print(graph)

    graph.add_edges("Warszawa", "Poznań")  # if vertex already exists in a graph
    print(graph)

    graph.add_edges("Wroclaw", "Poznań")  # if vertex is not in a graph
    print(graph)

    print(graph.dfs("Krakow"))

