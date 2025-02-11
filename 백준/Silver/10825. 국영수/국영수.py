import sys
input = sys.stdin.readline

T = int(input())
arr = []
for _ in range(T):
    name, kor, eng, math = map(str, input().split())
    kor, eng, math = int(kor), int(eng), int(math)
    arr.append((name, kor, eng, math))

arr = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])