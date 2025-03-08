n,d = map(int,input().split())
Allmoney = 0
time = 0

for i in range(n):
    money = sorted(map(int,input().split()))
    # money = list(money)
    # money.sort()

    if money[2] - money[0] >= d:
        Rmoney = sum(money) // 3
        time += 1
    else:
        Rmoney = 0

    Allmoney += Rmoney

print(time,Allmoney)