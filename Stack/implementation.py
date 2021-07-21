stack=[]
def push(val):
    stack.append(val)
def pop():
    return stack.pop()
def isEmpty():
    return len(stack)==0

push(10)
push(2)
push(3)
pop()
pop()
print(stack)
