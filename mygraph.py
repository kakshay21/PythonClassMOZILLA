#Graph ADT
#This ADT is for directed graph with no parallel edges
#For undirected graphs, during insertion and deletion, supply the values in both the directions
#The input is the weighted adjacent list
#Assume the weight as 1 for unweighted graph

class Graph:

	class Vertex:
		
		# Initialzing the required values
		def __init__(self):
			self.name=""
			self.adjacent=[]
	
	
	# Intializing the required values
	def __init__(self):
		self.n_ver=0
		self.n_edge=0
		self.vertices=[]
		self.corres_edges=[]

	# Input graph
	def give_graph(self):
		print "Enter the vertice name, enter 0 when done"
		i=raw_input()
		while i!='0':
			ver=self.Vertex()
			ver.name=i
			self.vertices.append(ver)
			self.n_ver+=1
			i=raw_input()
		count=0
		print "Enter 1 if there exists and edges, 0 otherwise"
		while count<self.n_ver:
			mark=0
			while mark<self.n_ver:
				edges=[]
				print "Is there an edge between ",self.vertices[count].name,"and ",self.vertices[mark].name," : "
				i=input()
				if i==1:
					print "What is the weight?"
					x=input()
					self.n_edge+=1
					edges.append(self.vertices[mark].name)
					edges.append(x)
					self.vertices[count].adjacent.append(edges)
				mark+=1
			count+=1
	
	# Printing the graph
	def print_graph(self):
		print "Neighbour vertex,weight is the format"
		count=0
		while count<self.n_ver:
			print self.vertices[count].name
			print self.vertices[count].adjacent
			count+=1
	
	# Adjacent to a vertice v
	def adjacent(self,v):
		i=0
		while self.vertices[i].name!=v:
			i+=1
		print self.vertices[i].adjacent
	
	# Deleting a vertex
	def deleteVertex(self,v):
		self.n_ver-=1
		for i in self.vertices:
			for j in i.adjacent:
				if j[0]==v:
					i.adjacent.remove(j)
		for i in self.vertices:
			if v==i.name:
				self.vertices.remove(i)
		self.print_graph()
	
	# Inserting a vertex
	def insertVertex(self):
		i=raw_input("Enter the vertex name : ")
		ver=self.Vertex()
		ver.name=i
		self.n_ver+=1
		mark=0
		while mark<self.n_ver-1:
			edges=[]
			print "Is there an edge between ",ver.name,"and ",self.vertices[mark].name," : "
			i=input()
			if i==1:
				print "What is the weight?"
				x=input()
				self.n_edge+=1
				self.vertices[mark].adjacent.append([ver.name,x])
				edges.append(self.vertices[mark].name)
				edges.append(x)
				ver.adjacent.append(edges)
			mark+=1
		self.vertices.append(ver)
		self.print_graph()
	
	# Deleting an edge
	def deleteEdge(self):
		self.n_edge-=1
		print "Enter the two vertices of the edge to be deleted"
		x=raw_input()
		y=raw_input()
		for i in self.vertices:
			if i.name==x:
				for j in i.adjacent:
					if j[0]==y:
						i.adjacent.remove(j)
						break
		self.print_graph()
		
	# Inserting an edge
	def insertEdge(self):
		self.n_edge+=1
		print "Enter the two vertices of the edge to be added"
		x=raw_input()
		y=raw_input()
		w=input("Enter the weight : ")
		i=0
		while self.vertices[i].name!=x:
			i+=1
		self.vertices[i].adjacent.append([y,w])
		self.print_graph()
		
	# Breath First Traversal
	def BFS(self,root):
		visited=[]
		bfs=[]
		queue=[]
		bfs.append([root])
		visited.append(root)
		queue.append(root)
		while len(queue):
			popped=queue.pop(0)
			for i in self.vertices:
				if i.name==popped:
					temp=[]
					for j in i.adjacent:
						if j[0] not in visited:
							queue.append(j[0])
							visited.append(j[0])
							temp.append(j[0])
					bfs.append(temp)
		print bfs
		
	# Depth First Traversal
	def DFS(self,root):
		bfs=self.BFS(root)
		i=0
		dfs=[]
		i=0
		while bfs[i]!=[]:
			while bfs[i][i]!= None:
				dfs.append(bfs[i][i])
			i+=1
		print dfs
		
	# Total number of vertices
	def num_vertices(self):
		return self.n_ver

	# Total number of edges
	def num_edges(self):
		return self.n_edge
	
