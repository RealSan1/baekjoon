import sys
input = sys.stdin.readline

S, E = map(int, input().split())
for i in range(S, E+1):    
    if str(i) == str(i)[::-1]:
        print("Palindrome!")
    else:
        print(i)