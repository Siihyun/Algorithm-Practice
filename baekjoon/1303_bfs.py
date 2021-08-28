from collections import deque

m,n = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
w = b = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,team):
  queue = deque([[x,y]])
  visited[x][y] = 1
  answer = 1

  while queue:
    cur_x, cur_y = queue.popleft()

    for i in range(4):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
      if visited[nx][ny] == 0 and graph[nx][ny] == team:
        visited[nx][ny] = 1
        queue.append([nx,ny])
        answer += 1
  
  return answer


for i in range(n):
  for j in range(m):
    if visited[i][j] == 0:
      if graph[i][j] == 'W':
        w += bfs(i,j,'W')**2
      else:
        b += bfs(i,j,'B')**2

print(w,b)