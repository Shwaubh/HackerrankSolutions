t = int(input())
cur = 1
for t_itr in range(t):
    n = int(input())
    for i in range(0,n):
        if i%2 == 0:
            cur = cur*2
        else:
            cur+=1
    print(cur)
    cur = 1