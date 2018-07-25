#Terminated due to timeout

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort(key=int)
[print(s) for s in data]