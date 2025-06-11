import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    A, K = map(str, input().split())
    try:
        eight = int(K, base=8)
    except:
        eight = 0
    try:
        ten = int(K, base=10)
    except:
        ten = 0
    try:
        sixteen = int(K, base=16)
    except:
        sixteen = 0
        
    print(A, eight, ten, sixteen)