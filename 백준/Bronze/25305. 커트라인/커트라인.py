N, K = map(int, input().split())
X = list(map(int, input().split()))

X.sort(reverse=True)
print(X[K-1])