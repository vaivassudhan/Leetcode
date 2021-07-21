def isValid(s):
        stack=[]
        mapopen={'(':0,'{':1,'[':2}
        mapclose={')':0,'}':1,']':2}
        for i in s:
            if(i=='(' or i=='[' or i=='{' ):
                stack.append(i)
            else:
                if(len(stack)==0):
                    return False
                if(mapclose[i]==mapopen[stack[-1]]):
                    stack.pop()
                else:
                    return False
                
        if(len(stack)==0):
            return True
        else:
            return False

s = '(([]))'
print(isValid(s))
