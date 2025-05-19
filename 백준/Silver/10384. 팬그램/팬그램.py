import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    V = input()
    arr = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
    for i in V:
        if i.isalpha():
            arr[i.lower()] += 1

    S = min(arr.values())
    if S > 2:
        print(f"Case {_+1}: Triple pangram!!!")
    elif S > 1:
        print(f"Case {_+1}: Double pangram!!")
    elif S > 0:
        print(f"Case {_+1}: Pangram!")
    else:
        print(f"Case {_+1}: Not a pangram")