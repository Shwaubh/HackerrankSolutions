n = int(input())
data = []
for i in range(n):
    data.append(list(map(int , input().rstrip().split())))
    a = abs(data[i][0] - data[i][2])
    b = abs(data[i][2] - data[i][1])
    # print(a , b)
    if a == b:
        print("Mouse C")
    elif a<b:
        print("Cat A")
    else:
        print("Cat B")