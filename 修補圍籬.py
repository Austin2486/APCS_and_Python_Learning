ans,a = 0,-1
n = int(input())
h = list(map(int,input().split()))

for i in h:
    a +=1
    if len(h)-1 > a > 0:
        if i == 0:
            if h[a-1] >= h[a+1]:
                ans += h[a+1]
                # print(ans)

            elif h[a-1] <= h[a+1]:
                ans += h[a-1]
                # print(ans)
        else:
            pass
            # print('else',ans)
    elif a == 0 and i == 0:
        ans += h[a+1]
    else:
        if i == 0:
            ans += h[a-1]
        else:
            pass

print(ans)