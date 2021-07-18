from collections import defaultdict
graph=defaultdict(list)
def addEdge(u,v):
    graph[u].append(v)
    graph[v].append(u)
def shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    for edge in range(n-1):
        u,v=map(int,input().split())
        addEdge(u,v)
    for query in range(q):
        inp=list(map(int,input().split()))
        k=inp[0]
        d=inp[1]
        v=inp[2:]
        res=0
        for i in range(k):
            for j in range(i+1,k):
                # print("FOR PAIR ",v[i],v[j])
                spath=shortest_path(graph,v[i],v[j])
                if(spath):
                    # print("SPATH ",spath)
                    # print("LEN OF SP & D",len(spath),d)
                    if(len(spath)-1==d):
                        res+=1

        print(res)

