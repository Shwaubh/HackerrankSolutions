n = int(input())
s = input()
k = int(input())
k%=26
for i in s:
    #print("string " ,i)
    if i.isalpha():
        x = ord(i)+k
        if(i.islower()):
            flag = True
            while flag:
                if x > 122:
                    x-=26
                else:
                    break
            print(chr(x),end='',sep='')
        else:
            flag = True
            while flag:
                if x > 90:
                    x -= 26
                else:
                    break
            print(chr(x), end='', sep='')
    else:
        print(i, end='', sep='')
