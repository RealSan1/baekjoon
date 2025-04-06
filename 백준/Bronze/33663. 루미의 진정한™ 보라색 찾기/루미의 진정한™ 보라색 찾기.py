import sys
input = sys.stdin.readline

H1, H2 = map(int, input().split())
S1, S2 = map(int, input().split())
V1, V2 = map(int, input().split())
R, G, B = map(int, input().split())

M = max(R, G, B)
m = min(R, G, B)
V = M
S = 255 * ((V - m) / V)

if V == R:
    H = 60 * ((G-B) / (V - m))
elif V == G:
    H = 120 + 60 * ((B-R) / (V - m))
elif V == B:
    H = 240 + 60 * ((R-G) / (V - m))

if H < 0:
    H += 360

if (H1 <= H <= H2) and (S1 <= S <= S2) and (V1 <= V <= V2):
    print('Lumi will like it.')
else:
    print('Lumi will not like it.')