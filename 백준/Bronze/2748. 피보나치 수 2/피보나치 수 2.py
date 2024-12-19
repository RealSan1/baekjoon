N = int(input())

memo = {}
def fin(n):
    if n in memo:
        return memo[n]
    
    if n < 2:
        return n
    
    else:
        memo[n] = fin(n-1) + fin(n-2)
        return memo[n]
    
print(fin(N))
    