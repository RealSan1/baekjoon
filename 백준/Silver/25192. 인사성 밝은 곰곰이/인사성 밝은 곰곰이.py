A = int(input())
history = set()
result = 0
for _ in range(A):
    N = input()
    if N == 'ENTER':
        result += len(history)
        history = set()
    else:
        history.add(N)

result += len(history)

print(result)