import sys
input = sys.stdin.readline

while True:
   arr = {}
   result = []
   N, M = map(int, input().split())
   if N == 0 and M == 0:
      break
   for _ in range(N):
      V = list(map(int, input().split()))
      for i in V:
         if i in arr:
            arr[i] += 1
         else:
            arr[i] = 1

   Big = sorted(set(arr.values()), reverse=True)[1]

   for i, j in sorted(arr.items(), key=lambda x: -x[1]):
      if j == Big:
         result.append(i)
   result.sort()
   print(*result)        