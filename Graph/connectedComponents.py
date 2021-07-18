from collections import defaultdict
graph=defaultdict(list)

def dfsUtil(visited,v):
    global graph
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if(visited[i]==False):
            dfsUtil(visited,i)

def connectedComponents(v):
    visited=[False]*v
    for i in range(v):
        if(visited[i]==False):
            dfsUtil(visited,i)
            print()


n=int(input())
m=int(input())
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
connectedComponents(n)