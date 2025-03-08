builds = int(input())
builds_h = list(map(int,input().split()))

# for _ in range(builds):
#     h = int(input())
#     builds_h.append(h)

ans = 1
x = 1
fly = 0
for i in builds_h[1:]:
    if i < builds_h[x-1]:
        ans += 1
        x += 1
        if fly < ans:
            fly = ans
    else:
        ans = 1
        x += 1

print(fly)