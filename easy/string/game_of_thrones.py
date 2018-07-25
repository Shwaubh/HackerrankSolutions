s = input()
x = len(s)
if x%2 == 0:
    st = set(s)
    for i in st:
        if s.count(i)%2!=0:
            print("NO")
            break
    else:
        print("YES")
else:
    st = set(s)
    flag = 1
    for i in st:
        if s.count(i)%2!=0:
            if flag == 1 and s.count(i)%2==1:
               flag = 0
            else:
                print("NO")
                break
    else:
        print("YES")