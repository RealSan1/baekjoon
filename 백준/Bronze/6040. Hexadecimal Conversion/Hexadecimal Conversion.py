import sys

A = sys.stdin.readline().strip()
result = int(A, 16) 
print(oct(result)[2:])  
