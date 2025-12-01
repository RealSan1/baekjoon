import sys
input = lambda: sys.stdin.readline().rstrip()

HG = {
    'a': 'aespa',
    'b': 'baekjoon',
    'c': 'cau',
    'd': 'debug',
    'e': 'edge',
    'f': 'firefox',
    'g': 'golang',
    'h': 'haegang',
    'i': 'iu',
    'j': 'java',
    'k': 'kotlin',
    'l': 'lol',
    'm': 'mips',
    'n': 'null',
    'o': 'os',
    'p': 'python',
    'q': 'query',
    'r': 'roka',
    's': 'solvedac',
    't': 'tod',
    'u': 'unix',
    'v': 'virus',
    'w': 'whale',
    'x': 'xcode',
    'y': 'yahoo',
    'z': 'zebra'
}

HG_length = {chr(i): len(HG[chr(i)]) for i in range(ord('a'), ord('z') + 1)}

S = input()
HG_char_list = []
start = 0
is_valid = True

while start < len(S):
    char = S[start]

    symbol = HG[char]
    length = HG_length[char]
    end = start + length

    part = S[start:end]

    if part != symbol:
        is_valid = False
        break
    
    HG_char_list.append(char)
    
    start = end

if is_valid:
    print('It\'s HG!')
    print(''.join(HG_char_list))
else:
    print('ERROR!')