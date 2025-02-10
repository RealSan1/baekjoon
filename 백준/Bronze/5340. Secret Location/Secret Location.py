arrA = []
for i in range(3):
    arrA.append(len(input().strip()))

arrB = []
for i in range(3):
    arrB.append(len(input().strip()))

print(f"Latitude {arrA[0]}:{arrA[1]}:{arrA[2]}")
print(f"Longitude {arrB[0]}:{arrB[1]}:{arrB[2]}")