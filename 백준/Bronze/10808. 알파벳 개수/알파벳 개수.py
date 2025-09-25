import sys
input = sys.stdin.readline

arr = {chr(i+97) : 0 for i in range(26)}

S = input()
for i in S:        
    if i in arr:
        arr[i] += 1
    
print(*arr.values())