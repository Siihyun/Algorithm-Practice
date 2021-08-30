
v = int(input())
e = int(input())

board = [[] for _ in range(v)]
visited = [0]*v

def dfs(start,depth):
  visited[start] = 1

  for v in board[start]:
    if visited[v]: continue
    depth = dfs(v,depth+1)
  
  return depth

for i in range(e):
  r,c = map(int,input().split())
  board[r-1].append(c-1)
  board[c-1].append(r-1)

print(dfs(0,0))