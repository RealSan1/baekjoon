import math

rh, rv, sh, sv = map(int, input().split())
N = int(input())
arr = []
for _ in range(N):
    rhi, rvi, shi, svi, price = map(int, input().split())
    horizontal = max(math.ceil(rh / rhi), math.ceil(sh / shi))
    vertical = max(math.ceil(rv / rvi), math.ceil(sv / svi))
    arr.append(horizontal * vertical * price)

    horizontal = max(math.ceil(rh / rvi), math.ceil(sh / svi))
    vertical = max(math.ceil(rv / rhi), math.ceil(sv / shi))
    arr.append(horizontal * vertical * price)

print(min(arr))
