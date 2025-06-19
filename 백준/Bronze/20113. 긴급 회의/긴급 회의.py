import sys
input = sys.stdin.readline

N = int(input())
arr = {i:0 for i in range(0, N+1)}
vote = list(map(int, input().split()))
for i in vote:
    arr[i] += 1

num = sorted(arr.items(), key=lambda x: -x[1])[:3]
res_1 = num[0]
res_2 = num[1]
res_3 = num[2]

if res_1[0] == 0 and res_2[1] != res_3[1]:
    print(res_2[0])
elif res_1[1] == res_2[1]:
    print("skipped")
elif res_1[1] > res_2[1]:
    print(res_1[0])