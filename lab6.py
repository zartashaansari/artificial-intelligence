'''from collections import deque    
class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, v, w):
        """Add an edge to the graph"""
        self.adj[v].append(w)
       
    def dfs(self, start):
        visited=[] 
        stack=deque()
        stack.append(start)
        visited.append(start)
        while(stack):
            last=stack.pop()
            if last not in visited:
                visited.append(last)
            for neighbour in self.adj[last]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    
        print(visited)
 
if __name__ == "__main__":
    g = Graph(13)
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
    g.dfs(1)
'''
#dfs implementation using stack
'''
from collections import deque


graph = {
   'A':['B','F','D','E'],
    'B' : ['K','J'],
    'K': ['N','M'],
    'N':[],
    'M':[],
    'J':[],
    'F':[],
    'D':['G'],
    'E':['C','H','I'],
    'I':['L'],
    'L':[],
    'C':[],
    'H':[],
    'G':[]
}

def dfs_stack(start, goal):
    visited = set()
    stack = [(start, [start])]  # Stack stores tuples of (node, path)
    
    while stack:
        node, path = stack.pop()
        
        if node == goal:
            return path  # Return the path if goal is found
        
        if node not in visited:
            visited.add(node)
            # Push children in reverse order to visit leftmost child first
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    
    return None  # Return None if goal is not reachable

# Perform DFS from 'A' to 'G'
start_node = 'A'
goal_node = 'G'
path = dfs_stack(start_node, goal_node)

print(f"DFS path from {start_node} to {goal_node}: {path}")
'''
'''
#python implementation of c++ code
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.adj = defaultdict(list)  # Adjacency list using defaultdict
    
    def add_edge(self, v, w):
        """Add an edge to the graph"""
        self.adj[v].append(w)
    
    def dfs_util(self, v, visited):
        """A recursive function used by DFS"""
        visited[v] = True
        print(v, end=" ")
        
        # Recur for all vertices adjacent to this vertex
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)
    
    def dfs(self, v):
        """DFS traversal of vertices reachable from v"""
        # Mark all vertices as not visited
        visited = [False] * self.V
        
        # Call the recursive helper function
        self.dfs_util(v, visited)

# Driver code
if __name__ == "__main__":
    # Create a graph given in the above diagram
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("Following is Depth First Traversal (starting from vertex 2)")
    g.dfs(2)'''