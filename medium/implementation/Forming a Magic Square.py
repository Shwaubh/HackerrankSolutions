s = []
i = 0
j = 0
for k in range(3):
    x = list(map(int, input().rstrip().split()))
    if 1 in x:
        i = k
        j = x.index(1)
    s.append(x)
i1 = i
j1 = j
t = [[0,0,0],[0,0,0],[0,0,0]]
cur = 1
t[i][j] = cur
flag = 0
while True:
    if flag == 0:
        i=i+1
        j=j+2
    else:
        i=i-1
        j=j+2
    if i==3:
        i=0
    if i==-1:
        i=2
    if j>=3:
        j-=3
    if t[i][j] ==  0:
        cur+=1
        t[i][j]=cur
        flag = 0
        if cur == 9:
            break
    else:
        flag = 1
no = 0
for i in range(3):
    for j in range(3):
        if t[i][j]!=s[i][j]:
            no+=abs(t[i][j]-s[i][j])

i,j = i1,j1
t = [[0,0,0],[0,0,0],[0,0,0]]
cur = 1
t[i][j] = cur
flag = 0
while True:
    if flag == 0:
        i=i+1
        j=j+1
    else:
        i=i+1
        j=j-1
    if j==3:
        j=0
    if i==3:
        i=0
    if j==-1:
        j=2
    if t[i][j] ==  0:
        cur+=1
        t[i][j]=cur
        flag = 0
        if cur == 9:
            break
    else:
        flag = 1
no1 = 0
for i in range(3):
    for j in range(3):
        if t[i][j]!=s[i][j]:
            no1+=abs(t[i][j]-s[i][j])
print(min(no , no1))