import sys
from collections import Counter
input = sys.stdin.readline

A = input().strip()
count = Counter(A)

odd_chars = [char for char, freq in count.items() if freq % 2 == 1]

if len(odd_chars) > 1:
    print("I'm Sorry Hansoo")
else:
    half = []
    center = ''

    for char in sorted(count.keys()):
        freq = count[char]
        half.append(char * (freq // 2))
        if freq % 2 == 1:
            center = char

    left = ''.join(half)
    print(left + center + left[::-1])
