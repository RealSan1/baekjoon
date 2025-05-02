import sys
input = sys.stdin.readline

arr = list(map(float, input().split()))

Tavg = sum(arr) / 10
V = 0
for i in arr:
    V += (i - Tavg) ** 2

result = (V / 9) ** 0.5

if result <= 1.0:
    print("COMFY")
else:
    print("NOT COMFY")