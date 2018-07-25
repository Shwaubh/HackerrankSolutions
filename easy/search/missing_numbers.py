import collections

m = int(input())
data_m = [int(x) for x in input().split()]
n = int(input())
data_n = [int(x) for x in input().split()]
min1 = min(data_m)
max1 = max(data_m)
d1 = collections.Counter(data_m)
d2 = collections.Counter(data_n)
for i in range(min1 , max1+1):
    x = d2[i] - d1[i]
    if x!= 0:
        print(i,end=" ")