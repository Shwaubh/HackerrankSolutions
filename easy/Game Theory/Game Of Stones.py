allow = [2,3,5]
for _ in range(int(input())):
    start = 1
    data = int(input())
    while data>0:
        if data - allow[2] not in allow and data - allow[2] >= 0:
            data-=allow[2]
            start+=1
            #print("1")
        elif data - allow[1] not in allow and data - allow[1] >= 0:
            start+=1
            data-=allow[1]
            # print("2")
        elif data - allow[0] not in allow and data - allow[0] >= 0:
            start+=1
            data-=allow[0]
            # print("3")
        else:
             data = data - allow[0]
             # print("4")
             if not data<0:
                start+=1
                # print("5")
    if start%2 == 1:
        print("Second")
    else:
        print("First")