#Graph ADT
#This ADT is for directed graph with no parallel edges
#For undirected graphs, during insertion and deletion, supply the values in both the directions
#The input is the weighted adjacent list
#Assume the weight as 1 for unweighted graph

class Graph:
    def __init__(self):
        self.graph = {}
 
    def insertEdge(self,u,v):
        self.graph[u]=v
 
    def BFS(self, root):
        visited = [0]*(len(self.graph))
        queue = []
        queue.append(root)
        visited[root] = 1
 
        while queue:
            root = queue.pop(0)
            print root,
            for i in self.graph.values():
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1

if __name__=='__main__':
	g = Graph()
	g.insertEdge(0, 1)
	g.insertEdge((0,1), 2)
	g.insertEdge(2, 0)
	g.insertEdge((2,3), 3)
	g.BFS(2)