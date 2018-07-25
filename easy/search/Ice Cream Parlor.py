q = int(input())
for _ in range(q):
    m = int(input())
    n = int(input())
    data = [int(x) for x in input().split()]
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]+data[j] == m:
                print(i+1,j+1)
                break