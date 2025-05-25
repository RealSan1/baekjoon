def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def generate_palindromes(limit):
    count = 0
    
    for i in range(10):
        if i > limit:
            break
        count += 1
    
    for half in range(1, 1000000):
        s = str(half)
        
        even_pal = int(s + s[::-1])
        if even_pal > limit:
            break
        if is_palindrome(even_pal // 10):
            count += 1
        
        for mid in '0123456789':
            odd_pal = int(s + mid + s[::-1])
            if odd_pal > limit:
                continue
            if is_palindrome(odd_pal // 10):
                count += 1

    return count

N = int(input())
print(generate_palindromes(N))
