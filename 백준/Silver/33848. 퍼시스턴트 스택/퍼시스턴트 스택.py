import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

Q = int(input())
stack = [None] * (Q + 1)
size = [0] * (Q + 1)

class Node:
    __slots__ = ('val', 'prev')
    def __init__(self, val, prev):
        self.val = val
        self.prev = prev

cur = 0
for _ in range(Q):
    q = input().split()
    t = int(q[0])

    if t == 1:
        cur += 1
        x = int(q[1])
        stack[cur] = Node(x, stack[cur - 1])
        size[cur] = size[cur - 1] + 1

    elif t == 2:
        cur += 1
        stack[cur] = stack[cur - 1].prev
        size[cur] = size[cur - 1] - 1

    elif t == 3:
        j = int(q[1])
        cur = cur - j

    elif t == 4:
        print(size[cur])

    elif t == 5: 
        if size[cur] == 0:
            print(-1)
        else:
            print(stack[cur].val)
