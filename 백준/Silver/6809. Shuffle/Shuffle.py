import sys
input = sys.stdin.readline

mapping = {}
reverse_mapping = {}

for i in range(27):
    A = input().strip() 
    B = chr(65 + i) if i < 26 else '_'
    mapping[B] = A
    reverse_mapping[A] = B  # 역변환용

N = int(input().strip())
T = input().strip()

def apply_cipher(text, times):
    if times == 0:
        return text 

    current = text
    while times > 0:
        if times % 2 == 1: 
            current = "".join(mapping[c] for c in current)
        mapping.update({c: mapping[mapping[c]] for c in mapping})
        times //= 2

    return current

result = apply_cipher(T, N)
print(result)
