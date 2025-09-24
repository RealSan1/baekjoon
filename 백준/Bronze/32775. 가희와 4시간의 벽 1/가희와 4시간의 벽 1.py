import sys
input = sys.stdin.readline

S = int(input()) # 철도 소요시간
F = int(input()) # 공항 소요시간

if S > F:
    print("flight")
else:
    print("high speed rail")