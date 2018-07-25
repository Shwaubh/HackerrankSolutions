n = int(input())
dem = "hackerrank"
cur = 0
for i in range(n):
    s = input()
    for i in s:
        if i == dem[cur]:
            cur+=1
        if cur == 10:
            print("YES")
            break
    else:
        print("NO")
    cur = 0