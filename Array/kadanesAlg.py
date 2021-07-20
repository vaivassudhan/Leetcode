def kadane(a):
    local_max = 0
    global_max = -999999
    for i in range(len(a)):
        local_max += a[i]
        if(global_max < local_max):
            global_max=local_max
        if(local_max < 0):
            local_max=0
    return global_max
a = [4,-1,2,1]
print(kadane(a))