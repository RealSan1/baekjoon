N, M = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
hap = 0
result = 0

while end < N:
    hap += arr[end]
    
    while hap > M and start <= end:
        hap -= arr[start]
        start +=1
    
    if hap == M:
        result +=1
    
    end += 1
    

print(result)
