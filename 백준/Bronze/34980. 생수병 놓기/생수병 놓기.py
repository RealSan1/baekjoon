import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
day = input()
night = input()

dayC = day.count('w')
nightC = night.count('w')

if day == night:
    print("Good")
    exit()

if dayC == nightC:
    print("Its fine")
    exit()

if dayC > nightC:
    print("Oryang")
else:
    print("Manners maketh man")