import sys
input = sys.stdin.readline

tel = 'PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV'

T = int(input())
for _ in range(T):
    C, D, S = input().split()

    opcode = tel.index(C)
    Bbin = bin(int(D))[2:].zfill(11)

    if S == 'F':
        Btype = '0'
    else:
        Btype = '1'

    result = f"{bin(opcode)[2:].zfill(5)}{Bbin}{Btype}"
    result = int(result, base=2)

    if result >= (1 << 16):
        result -= (1 << 17)

    fixed = result / (2 ** 16)

    output = f"{fixed:.16f}".rstrip('0')
    if output[-1] == '.':
        output += '0'
    
    print(output)

