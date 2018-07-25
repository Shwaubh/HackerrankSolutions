

def convertIntoPalindrome(s):
    total = 0
    l = len(s)
    if s == s[::-1]:
        print(total)
        return
    for i in range(l//2):
        total = total + abs(ord(s[i])- ord(s[l-i-1]))
    print(total)

q = int(input())
for i in range(q):
    convertIntoPalindrome(input())

