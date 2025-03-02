import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    Class = list(map(int, input().split()))[1:]
    Class.sort()
    gap = 0
    for i in range(len(Class)-1):
        gap = max(gap, Class[i+1] - Class[i])
    
    print(f"Class {_+1}")
    print(f"Max {max(Class)}, Min {min(Class)}, Largest gap {gap}")
