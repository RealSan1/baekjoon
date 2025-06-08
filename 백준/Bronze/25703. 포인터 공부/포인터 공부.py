import sys
input = sys.stdin.readline

N = int(input())
print("int a;")
print(f"int *ptr = &a;")
if N > 1:
    print("int **ptr2 = &ptr;")

for i in range(2, N):
    print(f"int {'*' * (i+1)}ptr{i+1} = &ptr{i};")
