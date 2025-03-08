import sys
input = sys.stdin.readline

kg = float(input())
m = float(input())

BMI = kg / m ** 2

if BMI >= 25:
    print('Overweight')
elif BMI >= 18.5 and BMI < 25:
    print('Normal weight')
elif BMI < 18.5:
    print('Underweight')