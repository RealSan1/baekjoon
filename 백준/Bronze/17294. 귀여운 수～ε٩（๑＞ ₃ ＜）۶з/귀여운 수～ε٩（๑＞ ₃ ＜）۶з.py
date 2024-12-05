k = input()
arr = []
if len(k) == 1:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')

elif len(k) == 2:
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')

else:
    d = int(k[1]) - int(k[0])
    for i in range(len(k)):
        arr.append(int(k[0]) + i * d)

    if ''.join(map(str, arr)) == k:
        print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    else:
        print('흥칫뿡!! <(￣ ﹌ ￣)>')