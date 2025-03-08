smallist = -1
biggest = 101

menber = int(input())
score = list(map(int,input().split()))
print(*sorted(score))

for i in score:
    if smallist < i < 60:
        smallist = i
    elif 60 <= i < biggest:
        biggest = i

if smallist != -1 and biggest == 101:
    print(smallist)
    print('worst case')
elif smallist == -1 and biggest != 101:
    print('best case')
    print(biggest)
else:
    print(smallist)
    print(biggest)