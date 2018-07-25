q = int(input())
for q_itr in range(q):
    s1 = input()
    s2 = input()
    if not len(set(s1).intersection(set(s2))):
        print("NO")
    else:
        print("YES")