import sys
input = sys.stdin.readline

normal = {}
special = {}
service = {}

A, B, C = map(int, input().split())

for _ in range(A):
    name, price = input().split()
    normal[name] = int(price)

for _ in range(B):
    name, price = input().split()
    special[name] = int(price)

for _ in range(C):
    name = input().strip()
    service[name] = 0

T = int(input())

normal_sum = 0
special_sum = 0
service_count = 0

for _ in range(T):
    menu = input().strip()
    
    if menu in normal:
        normal_sum += normal[menu]
    elif menu in special:
        special_sum += special[menu]
    elif menu in service:
        service_count += 1

valid = True

if special_sum > 0 and normal_sum < 20000:
    valid = False

if service_count > 1:
    valid = False
elif service_count == 1 and normal_sum + special_sum < 50000:
    valid = False

print("Okay" if valid else "No")