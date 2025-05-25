#implementation pf priority queue
'''class priorityQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,prioritynum) :
        index=0
        while index<len(self.items) and self.items[index][1] <=prioritynum:
            index+=1
        self.items.insert(index,(data,prioritynum) )   
    def isempty(self):
        if len(self.items)==0:
            return True

    def pop(self):
        if self.isempty():
            print("queue is empty")
            return None
        else:   
            return self.items.pop(0)[0]
    def size(self):
        return len(self.items)        
   
pq=priorityQueue()
pq.push("mira",4)
pq.push("zartasha",1)
pq.push("ali",2)
pq.push("shayan",3)
while not pq.isempty():
    print(pq.pop())'''

#implementation of bfs
#making graph as a directory
'''
graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'K': ['N', 'M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
    'N': [],
    'M': [],
    'L': []
}

def bfs(graph,start,goal):
    visited=[]
    queue=[]
    queue.append(start)
    visited.append(start)
    while queue:
        node=queue.pop(0)
        
        if(node==goal):
            print("goal found",node)
            return
        else:
            print("at",node)    
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour) 
                visited.append(neighbour)   

bfs(graph,'A','L')
'''
'''
from collections import deque


class Graph:
    def _init_(self, vertices):
        self.v = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, v, w):
        """Add an edge to the graph"""
        self.adj[v].append(w)

    def bfs(self, s):
        """Perform BFS traversal starting from vertex s"""

        visited = [False] * self.v

        queue = deque()

        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.popleft()
            print(s, end=" ")
            for i in self.adj[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


if __name__ == "_main_":
    g = Graph(4)
    g.add_edge(1, 2)
    g.add_edge(1, 7)
    g.add_edge(1, 8)
    g.add_edge(2, 3)
    g.add_edge(2, 6)
    g.add_edge(8, 9)
    g.add_edge(8, 12)
    g.add_edge(9, 11)
    g.add_edge(9, 10)
    g.add_edge(3, 4)
    g.add_edge(3, 5)




    print("BFS traversal starting from vertex 2:")
    g.bfs(2)'''
'''
class Graph:
    def _init_(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
       

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")


graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 1)
graph.add_edge(2, 3)
graph.add_edge(4, 0)
graph.add_edge(4, 1)
graph.add_edge(4, 3)

graph.print_graph()'''