import sys
input = lambda: sys.stdin.readline().rstrip()

img = input()
size = len(img)
dot = img.count(':')
bar = img.count('_')

print(size + dot + (bar * 5))