import sys

A = list(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
left = A
right = []

for _ in range(N):
    M = sys.stdin.readline().rstrip()
    if M[0] == 'P':
        left.append(M[2:])

    elif M[0] == 'L':
       if len(left) > 0:
            right.append(left.pop())

    elif M[0] == 'D':
        if len(right) > 0:
            left.append(right.pop())

    elif M[0] == 'B': 
        if left:
            left.pop()

print("".join(left + list(reversed(right))))