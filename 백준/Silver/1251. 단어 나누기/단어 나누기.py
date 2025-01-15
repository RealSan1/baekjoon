word = list(input())
arr = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        A = word[:i][::-1]
        B = word[i:j][::-1]
        C = word[j:][::-1]
        arr.append("".join(A+B+C))

arr.sort()
print(arr[0])