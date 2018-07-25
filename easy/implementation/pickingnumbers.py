n = int(input())
data = list(map(int, input().rstrip().split()))
data.sort()

cur = 0

for i in range(len(data)):
    a = data.count(data[i])
    b = data.count(data[i]+1)
    cur = max(cur , a+b)
    # print("Outer : " ,i,a,b,cur)
    if b == 0:
        i = cur+1
        # print("Inner : ",i)
    else:
        i = a+1

print(cur)
