import textwrap as t

def num_change(s):
    if s=='SOS':
        return 0
    else:
        x = 0
        if s[0]!='S':
            x+=1
        if s[1]!='O':
            x+=1
        if s[2]!='S':
            x+=1
        return x

s = t.wrap(input(),3)
x = 0
for i in s:
    x = x + num_change(i)
print(x)