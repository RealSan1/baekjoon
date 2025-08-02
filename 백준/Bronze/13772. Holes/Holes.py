import sys
input = sys.stdin.readline

arr = {
    'A': 1, 'B': 2, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
    'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 1, 'P': 1, 
    'Q': 1, 'R': 1, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
    'Y': 0, 'Z': 0, ' ': 0
}

N = int(input())
for _ in range(N):
    num = input().strip()
    res = 0
    for i in num:
        res += arr[i]
    print(res)
