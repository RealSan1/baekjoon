def vic(Team):
    L = Team.count('L') + N.count('L')
    O = Team.count('O') + N.count('O')
    V = Team.count('V') + N.count('V')
    E = Team.count('E') + N.count('E')

    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

dic = {}
N = input()
A = int(input())
vic(N)

for i in range(A):
    Team = input()
    dic[Team] = vic(Team)

sorted_data = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
dic = dict(sorted_data)

print(list(dic.keys())[0])