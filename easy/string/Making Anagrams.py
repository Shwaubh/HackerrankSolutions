"""
STILL
INCOMPLETE
"""

s1 = input()
s2 = input()
s = set(s1).intersection(s2)
x = len(s1) + len(s2) - 2*len(s)
print(s , x)