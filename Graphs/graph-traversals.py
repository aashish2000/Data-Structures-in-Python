def Graph():
	graph={}
	return(graph)

def addPath(n1,n2,graph):
	try:
		graph[n1].append(n2)
	except:
		graph[n1]=[n2]
	#Uncomment Below lines if Graph is Undirected
	'''try:
		graph[n2].append(n1)
	except:
		graph[n2]=[n1]'''

	return(graph)

def bfs(graph,start):
	n=len(graph)
	visited=[False]*n

	queue=[start]

	ans=[]
	while(queue!=[]):
		node=queue.pop(0)
		ans.append(node)
		visited[node]=True
		
		for i in graph[node]:
			if(visited[i]==False):
				queue.append(i)
		
	return(ans)

def dfs(graph,start):
	n=len(graph)
	visited=[False]*n

	stack=[start]

	ans=[]
	while(stack!=[]):
		node=stack.pop()
		ans.append(node)
		visited[node]=True
		
		for i in graph[node]:
			if(visited[i]==False):
				stack.append(i)
		
	return(ans)

graph = Graph() 
graph=addPath(0, 1, graph) 
graph=addPath(0, 2, graph) 
graph=addPath(1, 2, graph) 
graph=addPath(2, 0, graph) 
graph=addPath(2, 3, graph) 
graph=addPath(3, 3, graph) 


print(" ".join(map(str,bfs(graph,2))))
print(" ".join(map(str,dfs(graph,2))))