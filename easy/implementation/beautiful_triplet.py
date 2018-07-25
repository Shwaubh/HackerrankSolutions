nd = input().split()
n = int(nd[0])
d = int(nd[1])
arr = list(map(int, input().rstrip().split()))
total = 0
for i in arr:
    if i+d in arr:
        if i+d+d in arr:
            total+=1
            #print( i , i+d , i+d+d)
    if i+d+d > arr[n-1]:
        #print(i+6 , " breaked ")
        break
print(total)