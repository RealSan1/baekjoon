import sys
input = sys.stdin.readline

N = int(input())
S = input()
result = 0
result += S.count('a')
result += S.count('i')
result += S.count('u')
result += S.count('e')
result += S.count('o')
print(result)