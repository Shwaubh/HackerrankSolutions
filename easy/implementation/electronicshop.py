ops = input().split()
s = int(ops[0])
mm = int(ops[1])
nn = int(ops[2])
m = list(map(int , input().rstrip().split()))
n = list(map(int , input().rstrip().split()))

max = -1
# for i in m:
#     for j in n:
#         a = i+j
#         # print("max is ",a)
#         if a == s:
#             print(a)
#             exit()
#         elif a < s:
#             if a > max:
#                 max = a
#         else:
#             pass
# print(max)

m.sort()
n.sort()
for i in m:
    for j in n:
        a = i+j
        if a == s:
             print(a)
             exit()
        elif a > s:
            break
        else:
            if a > max:
               max = a

print(max)