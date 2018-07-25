def list_total(s = ''):
    cur = s[0]
    lis = []
    x = 0
    i = 0
    while i < len(s):
        if s[i] == cur:
            if s[i].islower():
                x = x + ord(s[i]) - 96
                lis.append(x)
            else:
                x = x + ord(s[i]) - 64
                lis.append(x)
            i+=1
        else:
            cur = s[i]
            x = 0
    return lis
s = input()
lis = list_total(s)
n = int(input())
for i in range(n):
    l = int(input())
    if  l in lis:
        print("YES")
    else:
        print("NO")