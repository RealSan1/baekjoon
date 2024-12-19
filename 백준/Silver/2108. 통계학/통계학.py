from collections import Counter
import sys

N = sys.stdin.readline

arr = []
for i in range(int(input())):
    arr.extend(map(int, input().split()))

arr.sort()
counter = Counter(arr)
max_freq = max(counter.values())
modes = [num for num, freq in counter.items() if freq == max_freq]


if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]

Mean = round(sum(arr) / len(arr))
if Mean == -0:
    Mean = 0
else:
    Mean = int(Mean)


print(Mean) # 산술평균
print(arr[len(arr)//2]) # 중앙 값
print(mode) # 최빈값
print(max(arr)-min(arr)) # 범위