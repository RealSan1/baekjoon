import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    Title, Time = map(str, input().split(','))    
    res = ''
    res += Title + " - "
    Time = int(Time)
    Year = Time//60//24//365
    if Year > 0:
        res += str(Year) + " year(s) "
    Day = Time//60//24%365
    if Day > 0:
        res += str(Day) + " day(s) "
    Hour = Time//60%24
    if Hour > 0:
        res += str(Hour) + " hour(s) "
    Minute = Time%60
    res += str(Minute) + " minute(s)"

    print(res)