T = int(input())
A = input()
front, end = A.split("*")

for _ in range(T):
    word = input()
    if len(word) >= len(front) + len(end) and word.startswith(front) and word.endswith(end):
        print("DA")
    else:
        print("NE")