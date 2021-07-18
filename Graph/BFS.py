from collections import defaultdict
graph=defaultdict(list)
n=int(input())
m=int(input())
visited=[False]*(n)
q=[]
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
print("Enter start node")
s=int(input())
visited[s]=True
q.append(s)
while(q):
    s=q.pop(0)
    print(s,end=" ")
    for i in graph[s]:
        if(visited[i]==False ):
            q.append(i)
            visited[i]=True
    


