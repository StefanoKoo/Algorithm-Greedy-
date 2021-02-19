## Link : https://www.acmicpc.net/problem/6087

w, h = map(int,input().split())
lazer = []

for _ in range(h):
    lazer.append(input())
    
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

mirror = [[] for _ in range(h)]
queue = []

for i in range(h):
    for j in range(w):
        if lazer[i][j] ==  'C':
            queue.append([i,j])
        if lazer[i][j] != '*':
            mirror[i].append(-1)
        else:
            mirror[i].append(lazer[i][j])
            
            
def bfs(y,x):
    q = []
    q.append([y,x])
    
    mirror[y][x] = 0
    while q:
        y,x = q.pop(0)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            while 0 <= ny < h and 0 <= nx < w:
                if mirror[ny][nx] == '*':
                    break
                if mirror[ny][nx] == -1:
                    mirror[ny][nx] = mirror[y][x] + 1
                    q.append([ny,nx])
                nx += dx[i]
                ny += dy[i]
                
                
                
bfs(queue[0][0],queue[0][1])
print(mirror[queue[1][0]][queue[1][1]] - 1)
