m,n = map(int,input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
w = b = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,team,count=1):
  visited[x][y] = 1
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue
    if visited[nx][ny] == 0 and graph[nx][ny] == team:
      count = dfs(nx,ny,graph[nx][ny],count+1)
  
  return count



for i in range(n):
  for j in range(m):
    if visited[i][j] == 0:
      if graph[i][j] == 'W':
        w += dfs(i,j,'W')**2
      else:
        b += dfs(i,j,'B')**2

print(w,b)