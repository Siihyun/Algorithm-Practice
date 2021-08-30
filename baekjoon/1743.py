import sys
sys.setrecursionlimit(100000)

r,c,n = map(int, input().split())
board = [[0]*c for _ in range(r)]
visited = [[0]*c for _ in range(r)]
answer = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,depth):
  visited[x][y] = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny < 0 or nx >= r or ny >= c:
      continue
    if visited[nx][ny] == 0 and board[nx][ny] == 1:
      depth = dfs(nx,ny,depth+1)
  
  return depth



for i in range(n):
  row, col = map(int, input().split())
  board[row-1][col-1] = 1

for i in range(r):
  for j in range(c):
    if visited[i][j] == 0 and board[i][j] == 1:
      answer = max(answer,dfs(i,j,1))

print(answer)
    