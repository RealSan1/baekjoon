import sys
input = sys.stdin.readlines()

for i in input:
    while True:
        result= i.replace('BUG','')

        if 'BUG' in result:
            i = result
        else: 
            print(result,end="") 
            break
