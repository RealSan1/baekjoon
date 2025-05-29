import sys
input = sys.stdin.readline

B = int(input())
Watermelon = int(input())
Pomegranates = int(input())
Nuts = int(input())

if B >= Watermelon:
    print("Watermelon")
elif B >= Pomegranates:
    print("Pomegranates")
elif B >= Nuts:
    print("Nuts")
else:
    print("Nothing")