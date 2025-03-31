import sys
input = sys.stdin.readline

mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 
            11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 
            20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
while True:
    A = input().strip()
    if A == 'R0C0':
        break
    result = ''
    R = int(A[1:A.find('C')])
    C = int(A[A.find('C')+1:])
    
    while C > 0:
        C -= 1
        result += mapping[C % 26 + 1]
        C //= 26
    
    print(f"{result[::-1]}{R}")