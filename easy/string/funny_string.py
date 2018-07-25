q = int(input())
pri = []
for q_itr in range(q):
    s = input()
    r = s[::-1]
    for i in range(len(s)-1):
        #print(i , s , r , ord(s[i]) , ord(s[i+1]) , ord(r[i]) , ord(r[i+1]))
        if(abs(ord(s[i])-ord(s[i+1])) == abs(ord(r[i])-ord(r[i+1]))):
            pass
        else:
            pri.append("NOT FUNNY")
            break
    else:
        pri.append("FUNNY")
for i in pri:
    print(i)