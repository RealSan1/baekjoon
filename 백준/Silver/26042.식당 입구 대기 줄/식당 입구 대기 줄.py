import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
queue = deque()
max_len = 0
min_back = sys.maxsize

for _ in range(n):
    cmd = input().split()
    if cmd[0] == '1':
        student = int(cmd[1])
        queue.append(student)

        qlen = len(queue)
        if qlen > max_len:
            max_len = qlen
            min_back = student 
        elif qlen == max_len:
            min_back = min(min_back, student)
    else:
        queue.popleft()

print(max_len, min_back)
