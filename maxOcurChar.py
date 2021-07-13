s=input()
map={}
maxv=0
for i in s:
    if(i in map):
        map[i]+=1
        if(maxv<map[i]):
            maxv=map[i]
    else:
        map[i]=1
for i in map:
    if(map[i]==maxv):
        print(i)
        break