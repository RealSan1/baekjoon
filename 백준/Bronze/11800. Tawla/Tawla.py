import sys
input = lambda: sys.stdin.readline().rstrip()

p1 = {1 : "Yakk", 2 : "Doh", 3 : "Seh",
      4 : "Ghar", 5 : "Bang", 6 : "Sheesh"}

p2 = {1 : "Habb Yakk", 2 : "Dobara", 3 : "Dousa",
      4 : "Dorgy", 5 : "Dabash", 6 : "Dosh"}

for i in range(int(input())):
    num = list(map(int, input().split()))
    num.sort(reverse=True)

    if num[0] == num[1]:
        print('Case {}: {}'.format(i+1, p2[num[0]]))
    else:
        if num[0] == 6 and num[1] == 5:
            print('Case {}: Sheesh Beesh'.format(i+1))
        else:
            print('Case {}: {} {}'.format(i+1, p1[num[0]], p1[num[1]]))