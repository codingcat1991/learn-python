import collections


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_vertices(self):
        return list(self.gdict.keys())

    def add_vertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = set()

    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].add(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def find_edges(self):
        edge_name = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edge_name:
                    edge_name.append({nxtvrtx, vrtx})
        return edge_name

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for nxt in self.gdict[start] - visited:
            self.dfs(nxt, visited)
        return visited

    def bfs(self, start):
        seen, queue = {start}, collections.deque([start])
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for node in self.gdict[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)
        return seen


graph_elements = {"a": {"b", "c"},
                  "b": {"a", "d"},
                  "c": {"a", "d"},
                  "d": {"e"},
                  "e": {"d"}}

g = Graph(graph_elements)
# g.add_vertex("f")
# print(g.get_vertices())
# g.add_edge({'d', 'f'})
# print(g.find_edges())
#
g.dfs('a')
g.bfs('a')
