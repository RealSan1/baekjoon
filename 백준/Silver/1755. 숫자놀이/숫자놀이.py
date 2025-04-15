import sys
input = sys.stdin.readline

mapping = { 0 : "zero", 1 : "one", 2 : "two", 3: "three", 4 : "four"
           ,5: "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine" }
arr = []
N, M = map(int, input().split())
for i in range(N, M+1):
    if len(str(i)) == 1:
        arr.append([i, mapping[i]])
    else:
        num = str(i)
        temp = mapping[int(num[0])]
        temp += mapping[int(num[1])]
        arr.append([i, temp])


for i, (j, _) in enumerate(sorted(arr, key=lambda x: x[1])):
    print(j, end=' ')
    if (i + 1) % 10 == 0:
        print()