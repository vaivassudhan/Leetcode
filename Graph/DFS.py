from collections import defaultdict
graph=defaultdict(list)

visited=[False]*(n)
def dfs(g,v):
    global visited
    print(v,end=" ")
    for i in graph[v]:
        if(visited[i]==False):
            visited[i]=True
            dfs(g,v)
def dfsStack(g,v):
    global visited
    stack=[v]
    while(stack):
        v=stack.pop()
        if(visited[v]==False):
            print(v,end=" ")
            visited[v]=True
            for i in g[v]:
                if(visited[i]==False):
                    stack.append(i)



n=int(input())
m=int(input())
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
print("Enter start node")
s=int(input())
dfsStack(graph,s)


