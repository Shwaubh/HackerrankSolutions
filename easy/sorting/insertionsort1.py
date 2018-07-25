n = int(input())
arr = list(map(int, input().rstrip().split()))
data = arr[n-1]
for i in range(n-2 , -1 , -1):
    if arr[i]>data:
        arr[i+1] = arr[i]
        for j in arr:
            print(j,end=" ")
        print()
    if arr[i] <= data or i == 0:
        if i == 0 and not arr[i]<=data:
            arr[i] = data
        else:
            arr[i + 1] = data
        for j in arr:
            print(j,end=" ")
        break