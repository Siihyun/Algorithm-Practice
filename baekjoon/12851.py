from collections import deque

def bfs2(start,target):
  visited = [[-1,0] for _ in range(100001)]
  visited[start][0] = 0
  visited[start][1] = 1

  que = deque([start])

  while que:
    cur = que.popleft()
    
    for i in [cur-1, cur+1, cur*2]:
      if i > 100000 or i < 0:
        continue
      
      if visited[i][0] == -1:
        visited[i][0] = visited[cur][0] + 1
        visited[i][1] = visited[cur][1]
        que.append(i)
        #print(que)

      elif visited[i][0] == visited[cur][0] + 1:
        visited[i][1] += visited[cur][1]
    
  return visited[target][0], visited[target][1]

start, target = map(int, input().split())

depth, count = bfs2(start,target)
print(depth)
print(count)