def numodd(args = []):
    cur = 0
    for i in args:
        if i % 2 == 1:
            cur+=1
    return cur
n = int(input())
data = list(map(int, input().rstrip().split()))

if n == 2:
    a = numodd(data)
    if a % 2 == 1:
        print("NO")
    else:
        print(a)
    exit()

total = 0
i = 0

while i < n-1:
    a = data[i]
    b = data[i+1]
    #print("frs : ",numodd(data) , i )
    if (numodd(data) == 0):
        print(total)
        exit()
    elif (numodd(data) % 2 == 1):
        print("NO")
        exit()
    else:
        if a%2 == 0 and b%2 ==0:
            i = i + 2
        if a%2 == 1 and b%2 ==1:
            #print("came")
            i = i + 2
            total+=2
        if a%2 == 1 and b%2 ==0:
            total+=2
            data[i+0]+=1
            data[i+1]+=1
            i = i + 1
        if a%2 == 0 and b%2 ==1:
            i = i + 1
        # print("sec : ", numodd(data) , i)

print(total)
