import sys
input = lambda: sys.stdin.readline().rstrip()

B, C, D = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))
res = 0

burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

print(sum(burger) + sum(side) + sum(drink))
while B > 0 and C > 0 and D > 0:
    B -= 1
    C -= 1
    D -= 1
    res += (burger.pop(0) + side.pop(0) + drink.pop(0)) * 0.9
res += sum(burger) + sum(side) + sum(drink)

print(int(res))