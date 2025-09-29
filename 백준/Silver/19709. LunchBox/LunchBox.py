import sys
input = lambda: sys.stdin.readline().rstrip()

N, m = map(int, input().split())
school = []
for _ in range(m):
    school.append(int(input()))

school.sort()

res = 0
for i in school:
    if i <= N:
        N -= i
        res += 1

print(res)