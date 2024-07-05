from collections import defaultdict, deque

class Graph: 
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = defaultdict(list)

    def addVertex(self, v):
        self.adjList[v] = []

    def addEdge(self, v, w):
        self.adjList[v].append(w)

    def topologicalSort(self):
        inDegree = {v: 0 for v in self.adjList}
        for v in self.adjList:
            for neighbor in self.adjList[v]:
                inDegree[neighbor] += 1
            
        queue = deque([v for v in inDegree if inDegree[v] == 0])
        topologicalOrder = []

        while queue:
            vertex = queue.popleft()
            topologicalOrder.append(vertex)

            for neighbor in self.adjList[vertex]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topologicalOrder) != self.vertices:
            print("O grafo contém um ciclo e não pode ter uma ordenação topológica")
        else:
            print("A ordenação topológica do grafo é:")
            print(" ".join(topologicalOrder))

g = Graph(6)
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

for vertex in vertices:
    g.addVertex(vertex)

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'D')
g.addEdge('D', 'E')
g.addEdge('E', 'F')

g.topologicalSort()