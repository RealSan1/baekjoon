import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
for i in range(N, -1, -1):
    if i > 2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        print()
    elif i > 1:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i-1} bottle of beer on the wall.")
        print()
    elif i == 1:
        print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
        print(f"Take one down and pass it around, no more bottles of beer on the wall.")
        print()
    else:
        print(f"No more bottles of beer on the wall, no more bottles of beer.")
        if N != 1:
            print(f"Go to the store and buy some more, {N} bottles of beer on the wall.")
        else:
            print(f"Go to the store and buy some more, {N} bottle of beer on the wall.")
        