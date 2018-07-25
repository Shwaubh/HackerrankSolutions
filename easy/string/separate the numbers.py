import re
def separateNumbers(s , n):
    i = 0
    if len(s) == 1 or n==len(s):
        print("NO")
        return
    else:
        x = re.findall('.'*n,s)
        x.append(s[:])
        for i in range(1,len(x)):
            if int(x[i])-int(x[i-1]) == 1:
                pass
            else:
                break
        else:
            print(x , i)
            print("YES",x[0])
            return
        separateNumbers(s,n+1)
        return
q = int(input())
for i in range(q):
    separateNumbers(input(),1)