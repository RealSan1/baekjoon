N = int(input())
def fib(n):
    if n == 1 or n == 2:
        return 1  # 코드1
    else: 
        return (fib(n - 1) + fib(n - 2))
    
    
    

def fibonacci(n):
    var = 0
    if n <= 2: 
        return 1
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2
        var +=1

    return var

print(fib(N), fibonacci(N))