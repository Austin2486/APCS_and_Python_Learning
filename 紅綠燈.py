wait2 = 0
green,red = map(int,input().split())
people = int(input())
second = list(map(int,input().split()))
total = green + red

for i in second:
    wait = i % total
    if wait < green:
        pass
    else:
        wait = total - wait
        wait2 += wait
print(wait2)