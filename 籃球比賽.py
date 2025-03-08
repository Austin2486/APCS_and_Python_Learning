A1team = sum(map(int,input().split()))
B1team = sum(map(int,input().split()))
A2team = sum(map(int,input().split()))
B2team = sum(map(int,input().split()))
print(f'{A1team}:{B1team}''\n'f'{A2team}:{B2team}' )
if A1team > B1team:
    if A2team > B2team:
        print('Win')
    else:
        print('Tie')
else:
    if A2team < B2team:
        print('Lose')
    else:
        print('Tie')