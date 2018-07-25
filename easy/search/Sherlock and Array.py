q = int(input())
for _ in range(q):
    n = int(input())
    data = [int(x) for x in input().split()]
    whole = sum(data)
    left = 0
    right = whole - data[0]
    if len(data) == 1:
        print("YES")
    else:
        for i in range(1,len(data)):
            left = left + data[i - 1]
            right = right - data[i]
            if left>right:
                     print("NO")
                     break
            if left == right:
                print("YES")
                break