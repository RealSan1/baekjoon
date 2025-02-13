import sys
input = sys.stdin.readline

def is_palindrome(num):
    # str(num) == str(num)[::-1] 쓰면 느림
    if num < 10:
        return True
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return original == reversed_num

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 11:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def solve(N, M):
    result = []
    for num in range(N, M + 1):
        if num == 11 and N <= 11 <= M:
            result.append(11)
            continue
        if len(str(num)) % 2 != 0 and is_palindrome(num):
            if is_prime(num):
                result.append(num)
    
    for i in result:
        print(i)

N, M = map(int, input().split())
solve(N, M)
print(-1)