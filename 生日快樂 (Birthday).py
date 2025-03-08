months = [0,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31]
days = 0

nowM,nowD = map(int,input().split())
birthM,birthD = map(int,input().split())

if nowM == birthM:
    if birthD > nowD:
        print(birthD - nowD)
    elif birthD == nowD:
        print(0)
    else:
        minus_day = birthD - nowD
        print(365 + minus_day)

elif nowM < birthM:
    for i in range(nowM+1,birthM):
        days += months[i]               
    days = days + (months[nowM] - nowD) + (birthD)
    print(days)
else:
    for i in range(nowM+1,birthM+12):
        days += months[i]               
    days = days + (months[nowM] - nowD) + (birthD)
    print(days)