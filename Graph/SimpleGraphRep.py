from collections import defaultdict 
graph=defaultdict(list)
n=int(input())
m=int(input())
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
q=int(input())
for i in range(q):
    flag=False
    a,b=map(int,input().split())
    for j in (graph[a]):
        if(j==b):
            flag=True
    if(flag):
        print("YES")
    else:
        print("NO")
    
