import re

longest_word = "" 
while True:
    line = input()
    if 'E-N-D' in line:
        line = line.replace('E-N-D', '') 
        words = re.findall(r"[a-zA-Z-]+", line) 
        for word in words:
            if len(word) > len(longest_word): 
                longest_word = word
        break
    else:
        words = re.findall(r"[a-zA-Z-]+", line)
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

print(longest_word.lower()) 
