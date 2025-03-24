import sys
input = sys.stdin.readline

N = input().strip()
target = "UCPC"
index = 0 

for char in N:
    if char == target[index]:  
        index += 1
        if index == 4: 
            print("I love UCPC")
            exit()

print("I hate UCPC")
