import re

pattern = r"^(?=.*[aeiou])(?!.*[aeiou]{3})(?!.*[^aeiou]{3})(?!.*([^eo])\1)[a-z]+$"

while True:
    N = input()
    if N == 'end':
        break

    if re.match(pattern, N):
        print(f"<{N}> is acceptable.")
    else:
        print(f"<{N}> is not acceptable.")
