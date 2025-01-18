T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # 문서 개수 / 궁금 문서
    arr = list(map(int, input().split())) # 문서 개수
    queue = []
    for core, index in enumerate(arr):
        queue.append([index, core])
    count = 0

    while True:
        first = queue.pop(0)
        if max(queue, default=[0,0])[0] > first[0]:
            queue.append(first) # 맨 뒤로

        else:
            count += 1
            if first[1] == M:
                print(count)
                break



"""
1
3 2
2 2 3

1
"""