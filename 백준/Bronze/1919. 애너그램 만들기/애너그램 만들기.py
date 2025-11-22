import sys
input = lambda: sys.stdin.readline().rstrip()

A = input()
B = input()
res = 0
for i in A:
    if A.count(i) > B.count(i):
        A = A.replace(i, '', 1)
        res += 1

    elif A.count(i) == B.count(i):
        continue
    
    elif B.count(i) == 0:
        A = A.replace(i, '', 1)
        res += 1

for i in B:
    if B.count(i) > A.count(i):
        B = B.replace(i, '', 1)
        res += 1
    
    elif A.count(i) == B.count(i):
        continue
    
    elif A.count(i) == 0:
        B = B.replace(i, '', 1)
        res += 1


print(res)