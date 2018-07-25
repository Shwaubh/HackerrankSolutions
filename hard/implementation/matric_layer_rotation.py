ops = list(map(int , input().rstrip().split()))
m = ops[0]
n = ops[1]
r = ops[2]
data = []
layer = []
for i in range(m):
    data.append(list(map(int , input().rstrip().split())))
# print(m , n , r ,data)

for _ in range(m//2):
    layer.append({})
print(layer)
x=0
for minn in range(m//2):
    for i in range(x,m-x):
        for j in range(x,n-x):
            # if :
                pass