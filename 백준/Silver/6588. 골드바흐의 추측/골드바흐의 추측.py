import sys
input = sys.stdin.readline

T = 1000001
prime = [True] * T
for i in range(2, int(T * 0.5)+1):
    for j in range(i * i, T, i):
        if prime[j]:
            prime[j] = False

while True:
    num = int(input())
    if num == 0:
        break

    for i in range(3, num // 2 + 1, 2):
        if prime[i] and prime[num-i]:
            print(f"{num} = {i} + {num - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")
