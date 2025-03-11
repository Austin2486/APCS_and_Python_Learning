score,stone = 0,0
dic,dics = 0,[(0,1),(1,0),(0,-1),(-1,0)]
m,n,k,r,c = map(int,input().split())
nr,nc = (r,c)
maze = [list(map(int,input().split())) for _ in range(m)]
while maze[nr][nc] > 0:
    score,stone = ((maze[nr][nc]+score) % k),stone+1
    if score == 0:
        dic = (dic + 1) % 4
    maze[nr][nc] -= 1
    cr,cc = dics[dic]
    while not (0 <= nr + cr < m and 0 <= nc + cc < n and maze[nr + cr][nc + cc] > -1):
        dic = (dic + 1) % 4
        cr, cc = dics[dic]
    nr,nc = nr + cr, nc + cc

print(stone)