from collections import deque

n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  que = deque([[0,0]])
  graph[0][0] = 1

  while que:
    cur_x, cur_y = que.popleft()

    if cur_x == n-1 and cur_y == m-1:
      return

    for i in range(4):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
      if graph[nx][ny] == '1':
        graph[nx][ny] = graph[cur_x][cur_y] + 1
        que.append([nx,ny])


bfs()
print(graph[n-1][m-1])