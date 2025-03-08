ans = 0
a,b = map(int,input().split())
n = int(input())

for i in range(n):
    thing1 = 0
    thing2 = 0
    menber = list(map(int,input().split()))
    for x in menber:
        if x == 0:
            break
        elif x == a:
            thing1 += 1
        elif x == -a:
            thing1 -= 1
        elif x == b:
            thing2 += 1
        elif x == -b:
            thing2 -= 1
        else:
            pass
    if thing1 >= 1 and thing2 >= 1:
        ans += 1 
    else:
        pass

print(ans)