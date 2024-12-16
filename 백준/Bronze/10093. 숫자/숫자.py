A,B = map(int, input().split())
arr = []
if A > B:
    temp = A
    A = B
    B = temp

for i in range(A+1, B):
    arr.append(i)

print(len(arr))
print(*arr)