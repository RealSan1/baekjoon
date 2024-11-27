import re

result = re.findall('[A-Z]', input())
print(''.join(result))