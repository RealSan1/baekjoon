import sys
input = sys.stdin.readline

N, L, K = map(int, input().split())
arr = []
for _ in range(N):
    A, B = map(int, input().split()) # 쉬운 / 어려운
    arr.append([A, B])

i = 0
res = 0
while K != 0:
    try:
        if arr[i][1] <= L:
            arr.pop(i)
            res += 140
            i = -1
            K -=1
        i += 1
    except:
        try:
            i = 0
            temp = arr[0][i]
            if arr[0][i] <= L:
                arr.pop(i)
                res += 100
                i = -1
                K -=1
            
            if K > 0: # 반복문 탈출
                Bool = False
                for i in arr[0]:
                    if L >= i:
                        Bool = True
            
            if not Bool:
                break
                    
            i += 1
        except:
            break            

print(res)
