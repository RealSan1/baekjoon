import sys
input = sys.stdin.readline

arr = {}

while True:
    number = input().strip()
    if number == '000-00-0000':
        break
    
    if number in arr:
        arr[number] = True
    else:
        arr[number] = False

for i,j in sorted(arr.items(), key=lambda x: x[0]):
    if j:
        print(i)