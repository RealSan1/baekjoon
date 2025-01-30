N = int(input())
    
if N <= 9:
    print(str(N))
    
else:
    length = 1  
    count = 9   
    start = 1   
    total = 0   

    while total + length * count < N:
        total += length * count
        length += 1
        count *= 10
        start *= 10

    offset = N - total - 1
    number = start + offset // length
    digit_index = offset % length

    print(str(number)[digit_index])