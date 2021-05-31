from collections import deque

#input 
N,M,V = map(int,input().split())
graph = [[] for i in range(N+1)]

# make adj matrix
for i in range(M):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N+1):
  graph[i].sort()

visited = [False for i in range(N+1)]


def dfs(graph,cur,visited):
  visited[cur] = True
  print(cur,end=' ')
  adjs = graph[cur]
  for adj in adjs:
    if visited[adj]: continue
    dfs(graph,adj,visited)

def bfs(graph,V):
  visited = [False for i in range(N+1)]
  que = deque()
  que.append(V)

  while que:
    cur = que.popleft()
    if visited[cur] : continue
    print(cur,end=' ')
    visited[cur] = True
    adjs = graph[cur]
    for adj in adjs:
      que.append(adj)

dfs(graph,V,visited)
print()
bfs(graph,V)