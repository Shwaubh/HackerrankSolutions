t = int(input())
for t_itr in range(t):
    n = int(input())
    k = n
    cur = 0
    while n > 0:
        a = n % 10
        if a != 0:
            if k % a == 0:
                cur+=1
        n//=10
    print(cur)