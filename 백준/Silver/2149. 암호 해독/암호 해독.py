import sys
input = sys.stdin.readline

key = input().strip()
cipher = input().strip()

key_length = len(key)
rows = len(cipher) // key_length

sorted_positions = sorted(range(key_length), key=lambda x: (key[x], x))
original_positions = [sorted_positions.index(i) for i in range(key_length)]

matrix = [[''] * key_length for _ in range(rows)]
idx = 0
for col in range(key_length):
    original_col = sorted_positions[col]
    for row in range(rows):
        matrix[row][original_col] = cipher[idx]
        idx += 1

plaintext = ''
for row in matrix:
    plaintext += ''.join(row)

print(plaintext)
