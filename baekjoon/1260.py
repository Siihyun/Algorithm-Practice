from collections import deque

def dfs(graph, v, visited=[], answer =[]):
  visited.append(v)
  answer.append(v)

  for w in graph[v]:
    if w not in visited:
      answer = dfs(graph,w,visited,answer)
  return answer

def bfs(graph,v):
  queue = deque([v])
  visited = [v]
  answer = []

  while queue:
    next = queue.popleft()
    answer.append(next)

    for w in graph[next]:
      if w not in visited:
        visited.append(w)
        queue.append(w)
      
  return answer

n,m,v = map(int,input().split())
graph = dict()

for i in range(1,n+1):
  graph[i] = []

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for k in graph.keys():
  graph[k].sort()

print(' '.join(map(str,dfs(graph,v))))
print(' '.join(map(str,bfs(graph,v))))
