import sys
input = sys.stdin.readline

s1 = input().strip()  
s2 = input().strip()  

for char in s1:
    if '0' <= char <= '9':  
        s1 = s1.replace(char, " ") 

s1 = s1.replace(" ", "")

if s2 in s1:
    print(1) 
else:
    print(0)  
