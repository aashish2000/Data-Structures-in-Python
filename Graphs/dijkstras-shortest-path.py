import sys

def Graph(nodes):
	graph={}
	for i in range(nodes):
		graph[i]=[]
	return(graph)

def addPath(n1,n2,weight,graph):
	graph[n1].append([n2,weight])
	graph[n2].append([n1,weight])
	return(graph)

def generateMST(graph,start):
	temp_graph={}
	for i in graph:
		temp_graph[i]=graph[i]
	n=len(graph)

	visited=[False]*n
	mst=Graph(n)
	dist=[sys.maxsize]*n
	
	dist[start]=0

	vertex=start

	for i in range(n):
		visited[vertex]=True
		for nodeval in temp_graph[vertex]:
			node=nodeval[0]
			weight=nodeval[1]
			if(dist[node]>weight+dist[vertex]):
				dist[node]=weight+dist[vertex]

		minver=-1
		minval=sys.maxsize
		for i in range(n):
			if(visited[i]==False and dist[i]<minval):
				minval=dist[i]
				minver=i
		if(minver!=-1):
			mst[vertex].append([minver,minval-dist[vertex]])
			mst[minver].append([vertex,minval-dist[vertex]])
			vertex=minver

	return(mst,dist)


graph = Graph(9) 
graph=addPath(0, 1, 4, graph) 
graph=addPath(0, 7, 8, graph) 
graph=addPath(1, 2, 8, graph) 
graph=addPath(1, 7, 11, graph) 
graph=addPath(2, 3, 7, graph) 
graph=addPath(2, 8, 2, graph) 
graph=addPath(2, 5, 4, graph) 
graph=addPath(3, 4, 9, graph) 
graph=addPath(3, 5, 14, graph) 
graph=addPath(4, 5, 10, graph) 
graph=addPath(5, 6, 2, graph) 
graph=addPath(6, 7, 1, graph) 
graph=addPath(6, 8, 6, graph) 
graph=addPath(7, 8, 7, graph) 


mst,distances=generateMST(graph,0)

print(mst)
print(" ".join(map(str,distances)))

