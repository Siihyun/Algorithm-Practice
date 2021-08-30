from collections import deque

v = int(input())
e = int(input())

board = [[] for _ in range(v)]
visited = [0]*v

def bfs(start):
  visited[start] = 1
  que = deque([start])
  depth = -1

  while que:
    next = que.popleft()
    depth += 1

    for v in board[next]:
      if visited[v]:
        continue
      visited[v] = 1
      que.append(v)
  return depth

for i in range(e):
  r,c = map(int,input().split())
  board[r-1].append(c-1)
  board[c-1].append(r-1)

print(bfs(0))