def isKaprekar(num):
    sqr = num**2;
    instr = str(sqr)
    l = len(instr)
    if l > 1:
        a = int(instr[0:l//2])
    else:
        a=0
    b = int(instr[l//2:])
    if a+b == num:
        return True
    else:
        return False

p = int(input())
q = int(input())
num = 0

while p<=q:
    if(isKaprekar(p)):
        print(p , end=" ")
        num+=1
    p+=1
if num == 0:
    print("INVALID RANGE")