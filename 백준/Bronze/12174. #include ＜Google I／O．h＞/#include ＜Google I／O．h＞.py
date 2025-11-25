import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    B = int(input())
    A = input()
    arr = []
    for i in range(B):
        num = A[i*8:(i+1)*8]
        num = num.replace('O', '0')
        num = num.replace('I', '1')
        arr.append(num)
    res = ''
    for i in arr:
        res += chr(int(i, 2))
        
    print(f"Case #{_+1}: {res}")