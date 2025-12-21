import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
buffer = []
while True:
    A = int(input())
    if A == -1:
        break
    
    if A == 0:
        buffer.pop(0)
    elif A != 0 and len(buffer) < N:
        buffer.append(A)
if buffer:
    print(*buffer)
else:
    print("empty")